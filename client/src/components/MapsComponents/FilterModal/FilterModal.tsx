// FilterModal.tsx
import React, {useEffect, useState} from 'react';
import styles from './FilterModal.module.scss';

interface FilterModalProps {
    onClose: () => void;
}

const FilterModal: React.FC<FilterModalProps & { onApply: (filter: any) => void }> = ({
                                                                                          onClose,
                                                                                          onApply,
                                                                                      }: FilterModalProps & { onApply: (filter: any) => void }) => {
    const [filter, setFilter] = useState({
        departure: '',
        arrival: '',
        trainNumber: '',
        wagonNumber: '',
        quantity: '',
        loadingPoint: '',
        unloadingPoint: '',
        cargoType: '',
        netWeight: '',
        departureDate: '',
        loadingDate: '',
    });

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.target;
        setFilter((prevFilter) => ({ ...prevFilter, [name]: value }));
        console.log(filter);
    };

    useEffect(() => {
        onApply(filter);
    }, [filter, onApply]);



    return (
        <div className={styles.filterModal}>
            <div className={styles.header}>
                <h3>Фильтры</h3>
                <button className={styles.closeButton} onClick={onClose}>
                    &times;
                </button>
            </div>
            <div className={styles.inputGroup}>
                <div className={styles.inlineInputs}>
                    <input
                        type="text"
                        name="departure"
                        placeholder="Пункт отбытия"
                        value={filter.departure}
                        onChange={handleInputChange}
                    />
                    <input
                        type="text"
                        name="arrival"
                        placeholder="Пункт прибытия"
                        value={filter.arrival}
                        onChange={handleInputChange}
                    />
                    <input
                        type="date"
                        name="departureDate"
                        placeholder="Выберите дату"
                        value={filter.departureDate}
                        onChange={handleInputChange}
                    />
                </div>
            </div>
            <div className={styles.inputGroup}>
                <input
                    className={styles.trainNumber}
                    type="text"
                    name="trainNumber"
                    placeholder="Номер поезда"
                    value={filter.trainNumber}
                    onChange={handleInputChange}
                />
            </div>
            <div className={styles.inputGroup}>
                <div className={styles.inlineInputs}>
                    <input
                        type="text"
                        name="wagonNumber"
                        placeholder="Номер вагона"
                        value={filter.wagonNumber}
                        onChange={handleInputChange}
                    />
                    <input
                        type="text"
                        name="quantity"
                        placeholder="Количество"
                        value={filter.quantity}
                        onChange={handleInputChange}
                    />
                </div>
            </div>
            <div className={styles.inputGroup}>
                <div className={styles.inlineInputs}>
                    <input
                        type="text"
                        name="loadingPoint"
                        placeholder="Пункт загрузки"
                        value={filter.loadingPoint}
                        onChange={handleInputChange}
                    />
                    <input
                        type="text"
                        name="unloadingPoint"
                        placeholder="Пункт выгрузки"
                        value={filter.unloadingPoint}
                        onChange={handleInputChange}
                    />
                    <input
                        type="date"
                        name="departureDate"
                        placeholder="Выберите дату"
                        value={filter.departureDate}
                        onChange={handleInputChange}
                    />
                </div>
            </div>
            <div className={styles.inputGroup}>
                <div className={styles.inlineInputs}>
                    <input
                        type="text"
                        name="cargoType"
                        placeholder="Тип груза"
                        value={filter.cargoType}
                        onChange={handleInputChange}
                    />
                    <input
                        type="text"
                        name="netWeight"
                        placeholder="Масса нетто"
                        value={filter.netWeight}
                        onChange={handleInputChange}
                    />
                </div>
            </div>
        </div>
    );
};

export default FilterModal;
