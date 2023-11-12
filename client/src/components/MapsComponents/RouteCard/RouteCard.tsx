// RouteCard.tsx
import React from 'react';
import styles from './RouteCard.module.scss';

interface RouteCardProps {
    routeNumber?: string;
    status?: string;
    wagonType?: string;
    additionalInfo?: string;
    departureCity?: string;
    arrivalCity?: string;
    departureTime?: string;
    arrivalTime?: string;
    loadingPoints?: string[] | undefined;
    trainNumber?: string;
    wagons?: string[] | undefined;
    cargoType?: string;
    cargoWeight?: string;
    selected?: boolean;
    animated?: boolean;
    onClick?: () => void;
}

const RouteCard: React.FC<RouteCardProps> = ({
                                                 routeNumber,
                                                 status,
                                                 wagonType,
                                                 additionalInfo,
                                                 departureCity,
                                                 arrivalCity,
                                                 departureTime,
                                                 arrivalTime,
                                                 loadingPoints,
                                                 trainNumber,
                                                 wagons,
                                                 cargoType,
                                                 cargoWeight,
                                                 selected,
                                                 animated,
                                                 onClick,
                                             }) => {
    return (
        <div className={`${styles.routeCard} ${selected ? styles.selected : ''}`} onClick={onClick}>
            <div className={`${styles.animatedRouteCard} ${styles.gridContainer}`}>
                <div className={`${styles.routeInfo} ${styles.gridItem}`}>
                    {routeNumber && <h3 className={styles.routeNumber}>Маршрут: {routeNumber}</h3>}
                    {status && <p className={styles.status}>{status}</p>}
                </div>
                <div className={styles.progressBarContainer}>
                    <div className={styles.progressBarBackground}></div>
                    <div className={styles.progressBarFill}></div>
                </div>
                <div className={styles.detailsContainer}>
                    <div className={`${styles.leftDetails} ${styles.gridItem}`}>
                        {departureCity && (
                            <p className={styles.location}>
                                <strong>Отбыл: </strong>
                                {departureCity}
                            </p>
                        )}
                        {departureTime && <p className={styles.time}>{departureTime}</p>}
                        {trainNumber && (
                            <p className={styles.trainInfo}>
                                <strong>Поезд</strong> <br />
                                {trainNumber}
                            </p>
                        )}
                        {cargoType && (
                            <p className={styles.cargoInfo}>
                                <strong>Тип груза</strong> <br />
                                {cargoType}
                            </p>
                        )}
                    </div>
                    <div className={`${styles.rightDetails} ${styles.gridItem}`}>
                        {arrivalCity && (
                            <p className={styles.location}>
                                <strong>Прибыл: </strong>
                                {arrivalCity}
                            </p>
                        )}
                        {arrivalTime && <p className={styles.time}>{arrivalTime}</p>}
                        {wagons && wagons.length > 0 && (
                            <p className={styles.trainInfo}>
                                <strong>Вагоны</strong> <br />
                                {wagons.join('\n')}
                            </p>
                        )}
                        {cargoWeight && (
                            <p className={styles.cargoInfo}>
                                <strong>Масса груза</strong> <br />
                                {cargoWeight} кг
                            </p>
                        )}
                    </div>
                </div>
                {loadingPoints && loadingPoints.length > 0 && (
                    <div className={styles.loadingPointsContainer}>
                        <strong className={styles.loadingPointsTitle}>Пункты</strong>
                        <div className={styles.loadingPoints}>
                            {loadingPoints.map((point, index) => (
                                <div key={index} className={index % 2 === 0 ? styles.leftPoint : styles.rightPoint}>
                                    {point}
                                </div>
                            ))}
                        </div>
                    </div>
                        )}
            </div>
        </div>
    );
};

export default RouteCard;
