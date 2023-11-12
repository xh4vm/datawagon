// Notifications.tsx
import React from 'react';
import NotificationCard from './NotificationCard/NotificationCard';
import styles from './Notifications.module.scss';

const Notifications: React.FC = () => {
    // Генерация тестовых данных (можете заменить их своими реальными данными)
    const notificationData = [
        { time: '10:30', type: 'warning', information: 'Низкий уровень топлива' },
        { time: '12:45', type: 'error', information: 'Отсутствует соединение с сервером' },
        { time: '14:15', type: 'info', information: 'Новое обновление приложения доступно' },
        { time: '10:30', type: 'warning', information: 'Низкий уровень топлива' },
        { time: '12:45', type: 'error', information: 'Отсутствует соединение с сервером' },
        { time: '14:15', type: 'info', information: 'Новое обновление приложения доступно' },
        { time: '10:30', type: 'warning', information: 'Низкий уровень топлива' },
        { time: '12:45', type: 'error', information: 'Отсутствует соединение с сервером' },
        { time: '14:15', type: 'info', information: 'Новое обновление приложения доступно' },
        { time: '10:30', type: 'warning', information: 'Низкий уровень топлива' },
        { time: '12:45', type: 'error', information: 'Отсутствует соединение с сервером' },
        { time: '14:15', type: 'info', information: 'Новое обновление приложения доступно' },
        { time: '10:30', type: 'warning', information: 'Низкий уровень топлива' },
        { time: '12:45', type: 'error', information: 'Отсутствует соединение с сервером' },
        { time: '14:15', type: 'info', information: 'Новое обновление приложения доступно' },
        { time: '10:30', type: 'warning', information: 'Низкий уровень топлива' },
        { time: '12:45', type: 'error', information: 'Отсутствует соединение с сервером' },
        { time: '14:15', type: 'info', information: 'Новое обновление приложения доступно' },
        { time: '10:30', type: 'warning', information: 'Низкий уровень топлива' },
        { time: '12:45', type: 'error', information: 'Отсутствует соединение с сервером' },
        { time: '10:30', type: 'warning', information: 'Низкий уровень топлива' },
        { time: '12:45', type: 'error', information: 'Отсутствует соединение с сервером' },
        { time: '14:15', type: 'info', information: 'Новое обновление приложения доступно' },
        { time: '10:30', type: 'warning', information: 'Низкий уровень топлива' },
        { time: '12:45', type: 'error', information: 'Отсутствует соединение с сервером' }
    ];

    return (
        <div className={styles.notifications}>
            {notificationData.map((data, index) => (
                <NotificationCard
                    key={index}
                    time={data.time}
                    type={data.type}
                    information={data.information}
                />
            ))}
        </div>
    );
};

export default Notifications;
