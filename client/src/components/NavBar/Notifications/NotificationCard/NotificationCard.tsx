import React from 'react';
import styles from './NotificationCard.module.scss';

interface NotificationCardProps {
    time: string;
    type: string;
    information: string;
}

const NotificationCard: React.FC<NotificationCardProps> = ({ time, type, information }: NotificationCardProps) => {
    return (
        <div className={`${styles.notificationCard} ${styles[type]}`}>
            <div className={styles.time}>{time}</div>
            <div className={styles.content}>
                <div className={styles.icon}>{getIcon(type)}</div>
                <div className={styles.information}>{information}</div>
            </div>
        </div>
    );
};

const getIcon = (type: string): React.ReactNode => {
    switch (type) {
        case 'warning':
            return <span className={`${styles.icon} ${styles.warning}`}>⚠</span>;
        case 'error':
            return <span className={`${styles.icon} ${styles.error}`}>❌</span>;
        case 'info':
            return <span className={`${styles.icon} ${styles.info}`}>ℹ</span>;
        default:
            return null;
    }
};

export default NotificationCard;
