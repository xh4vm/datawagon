// LeftBar.tsx
import React, {useState} from 'react';
import FilterModal from '../MapsComponents/FilterModal/FilterModal';
import RouteCard from '../MapsComponents/RouteCard/RouteCard';
import styles from './LeftBar.module.scss';
import filterSvg from "../../assets/filter.svg"
import NavBar from '../NavBar/NavBar';


interface LeftBarProps {
    selectedMarker: any,
    setSelectedMarker: (markerId: any) => void,
    isAuthent: boolean,
    handleLogin: () => void,
}


const LeftBar: React.FC<LeftBarProps> = ({
                                                 selectedMarker,
                                                 setSelectedMarker,
                                                 isAuthent,
                                                 handleLogin,
                                             }: LeftBarProps) => {
        const [searchInput, setSearchInput] = useState("");
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

    const routeData = [
        {
            id: 1,
            cargoType: "Гениальность",
            routeNumber: "GENIUSES",
            wagonType: "AAAAAAA",
            status: "Загружен",
            additionalInfo: "4",
            loadingPoints: ["Чекпоинт №1", "Чекпоинт №2", "Чекпоинт №3", "Чекпоинт №4"],
            arrivalCity: "Золотое Место",
            arrivalTime: "11:00 12.11.2023",
            cargoWeight: "1 тонна",
            departureCity: "Начало пути",
            departureTime: "17:00 10.11.2023",
            trainNumber: "ALLAH",
            wagons: ["Таня", "Юля", "Кирилл", "Вадим", "Саша"],
            nodes: [[40, 50], [60, 70]]
        },
        {
            id: 2,
            cargoType: "НеГениальность",
            routeNumber: "НеGENIUSES",
            wagonType: "АИА",
            status: "В ремонте",
            additionalInfo: "4",
            loadingPoints: ["Чекпоинт №3", "Чекпоинт №643578", "Рай", "Ад"],
            arrivalCity: "Ад",
            arrivalTime: "11:00 12.11.2023",
            cargoWeight: "100000 тонна",
            departureCity: "РАССИЯ",
            departureTime: "17:00 10.11.2023",
            trainNumber: "БУДДА",
            wagons: ["1", "ывапгоапыво", "ываоывао", "ываовыао", "ываовыаоп"],
            nodes: [[37.5362921, 75.7611376], [32.5362099, 85.7668608]]
        },
        {
            id: 3,
            cargoType: "1241235",
            routeNumber: "НеGE3456742567NIUSES",
            wagonType: "34573457",
            status: "В ре445373457монте",
            additionalInfo: "4",
            loadingPoints: ["Чек43575437поинт №3", "Чекп457457оинт №643578", "Р457457ай"],
            arrivalCity: "А457457457д",
            arrivalTime: "11:00 12.11.2023",
            cargoWeight: "1004574574000 тонна",
            departureCity: "457457",
            departureTime: "14574577:00 10.11.2023",
            trainNumber: "БУДД457457А",
            wagons: ["1", "ыва457457пгоапыво", "ы457457ваоывао", "ываовыао", "ываовыаоп"],
            nodes: [[37.5347034, 55.7611376], [37.5362099, 55.7668608]]
        }
    ];
        const [isFilterModalVisible, setFilterModalVisible] = useState(false);

        const handleCardClick = (markerId: any) => {
            setSelectedMarker(markerId);
        };

        const handleSearchInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
            setSearchInput(event.target.value);
        };

        const handleFilterApply = (appliedFilter: any) => {
            setFilter(appliedFilter);
        };

        const filteredAndSortedData = routeData
            .filter((route) => {
                const searchValue = searchInput.toLowerCase();
                return (
                    route.routeNumber.toLowerCase().includes(searchValue) ||
                    route.loadingPoints.some((point) => point.toLowerCase().includes(searchValue))
                );
            })
            .filter((route) => {
                // Применяем фильтры из FilterModal
                return (
                    (!filter.departure || route.departureCity.toLowerCase().includes(filter.departure.toLowerCase())) &&
                    (!filter.arrival || route.arrivalCity.toLowerCase().includes(filter.arrival.toLowerCase())) &&
                    (!filter.trainNumber || route.trainNumber.toLowerCase().includes(filter.trainNumber.toLowerCase())) &&
                    (!filter.wagonNumber || route.wagons.some((wagon) => wagon.toLowerCase().includes(filter.wagonNumber.toLowerCase()))) &&
                    (!filter.quantity || route.additionalInfo.toLowerCase().includes(filter.quantity.toLowerCase())) &&
                    (!filter.loadingPoint || route.loadingPoints.some((point) => point.toLowerCase().includes(filter.loadingPoint.toLowerCase()))) &&
                    (!filter.unloadingPoint || route.loadingPoints.some((point) => point.toLowerCase().includes(filter.unloadingPoint.toLowerCase()))) &&
                    (!filter.cargoType || route.cargoType.toLowerCase().includes(filter.cargoType.toLowerCase())) &&
                    (!filter.netWeight || route.cargoWeight.toLowerCase().includes(filter.netWeight.toLowerCase())) &&
                    (!filter.departureDate || route.departureTime.toLowerCase().includes(filter.departureDate.toLowerCase())) &&
                    (!filter.loadingDate || route.arrivalTime.toLowerCase().includes(filter.loadingDate.toLowerCase()))
                );
            })
            .sort((a, b) => a.routeNumber.localeCompare(b.routeNumber));

        return (
        <div className={styles.leftBar}>
            <NavBar isAuthent={isAuthent} handleLogin={handleLogin}/>
            <div className={styles.formContainer}>
                <input type="text" placeholder="Search" value={searchInput} onChange={handleSearchInputChange} className={styles.searchInput} />
                <button onClick={() => {setFilterModalVisible(!isFilterModalVisible)
                console.log(isFilterModalVisible)}}
                    className={styles.filterButton}><img width={28} src={filterSvg} alt="Filter Icon" /></button>
            </div>
            <div className={styles.scrollContainer}>
                {isFilterModalVisible ? (
                    <FilterModal onClose={() => setFilterModalVisible(!isFilterModalVisible)}  onApply={handleFilterApply}/>
                ) : (
                    filteredAndSortedData.map((route, index) => (
                        <RouteCard
                            key={index}
                            routeNumber={route.routeNumber}
                            status={route.status}
                            wagonType={route.wagonType}
                            additionalInfo={route.additionalInfo}
                            departureCity={route.departureCity}
                            arrivalCity={route.arrivalCity}
                            departureTime={route.departureTime}
                            arrivalTime={route.arrivalTime}
                            loadingPoints={route.loadingPoints}
                            trainNumber={route.trainNumber}
                            wagons={route.wagons}
                            cargoType={route.cargoType}
                            cargoWeight={route.cargoWeight}
                            selected={route.id === selectedMarker}
                            onClick={() => handleCardClick(route.id)} // Обработчик клика на карточку
                        />))
                )}
            </div>
        </div>
    );
};

export default LeftBar;