// Support.tsx
import React, {useRef, useState} from 'react';
import styles from './Support.module.scss'; // Предполагается, что у вас есть файл стилей
import sendIcon from "../../../assets/send.svg"
import attachmentsIcon from "../../../assets/attachment.svg"

interface Message {
    text?: string;
    date: string;
    image?: string;
}

const Support: React.FC = () => {
    const [message, setMessage] = useState<string>('');
    const [messages, setMessages] = useState<Message[]>([]);
    const [selectedImage, setSelectedImage] = useState<File | null>(null);

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setMessage(event.target.value);
    };

    const handleAttachmentClick = () => {
        // Trigger input click when attachment button is clicked
        if (inputRef.current) {
            inputRef.current.click();
        }
    };

    const handleFileChange = async (event: React.ChangeEvent<HTMLInputElement>) => {
        const file = event.target.files && event.target.files[0];

        if (file) {
            const resizedImage = await resizeImage(file);

            setSelectedImage(resizedImage);

            // Clear the text message when an image is selected
            setMessage('');
        }
    };

    const resizeImage = (file: File): Promise<File> => {
        return new Promise((resolve) => {
            const reader = new FileReader();

            reader.onload = (event) => {
                const img = new Image();
                img.src = event.target?.result as string;

                img.onload = () => {
                    const canvas = document.createElement('canvas');
                    const ctx = canvas.getContext('2d');

                    const maxWidth = 250;
                    const maxHeight = 400;

                    let width = img.width;
                    let height = img.height;
                    let i = 0;
                    while (i < 3) {
                        i++
                        if (width > maxWidth || height > maxHeight) {
                            const aspectRatio = width / height;

                            if (width > height) {
                                width = maxWidth;
                                height = width / aspectRatio;
                            } else {
                                height = maxHeight;
                                width = height * aspectRatio;
                            }
                        } else {break}
                    }

                    canvas.width = width;
                    canvas.height = height;

                    if (ctx) {
                        ctx.drawImage(img, 0, 0, width, height);
                        canvas.toBlob((blob) => {
                            const resizedFile = new File([blob as Blob], file.name, {
                                type: 'image/jpeg', // or the appropriate file type
                                lastModified: Date.now(),
                            });
                            resolve(resizedFile);
                        }, 'image/jpeg');
                    }
                    console.log([width, height]);
                };
            };

            reader.readAsDataURL(file);
        });
    };

    const handleSendClick = () => {
        if (message !== '' || selectedImage) {
            const newMessage: Message = {
                text: message,
                date: new Date().toLocaleString(),
                image: selectedImage ? URL.createObjectURL(selectedImage) : undefined,
            };

            setMessages([...messages, newMessage]);
            setMessage('');
            setSelectedImage(null);
        }
    };

    const inputRef = useRef<HTMLInputElement>(null);

    return (
        <div className={styles.supportContainer}>
            <h2>Тех.Поддержка</h2>
            {/* Chat messages go here */}
            <div className={styles.dialogContainer}>
                {messages.map((msg, index) => (
                    <div key={index} className={styles.messageBox}>
                        {msg.image && <img src={msg.image} alt="Attached" className={styles.attachedImage}/>}
                        {msg.text && <div className={styles.messageText}>{msg.text}</div>}
                        <div className={styles.messageDate}>{msg.date}</div>
                    </div>
                ))}
            </div>
            {/* Input area */}
            <div className={styles.inputArea}>
                {/* Hidden input for file selection */}
                <input
                    ref={inputRef}
                    type="file"
                    accept="image/png, image/jpeg, image/jpg"
                    style={{ display: 'none' }}
                    onChange={handleFileChange}
                />

                {/* Attachment button */}
                <div className={styles.attachmentButton} onClick={handleAttachmentClick}>
                    <img width={32} height={32} src={attachmentsIcon} alt={"Attachment"}/>
                </div>

                {/* Message input */}
                <input
                    type="text"
                    placeholder="Type your message..."
                    value={message}
                    onChange={handleInputChange}
                    className={styles.messageInput}
                />

                {/* Send button */}
                <div className={styles.sendButton} onClick={handleSendClick}>
                    <img width={32} height={32} src={sendIcon} alt={"Send"}/>
                </div>
            </div>
        </div>
    );
};

export default Support;