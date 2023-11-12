// Main.tsx
import React, {useState} from 'react';
import LeftBar from '../../components/LeftBar/LeftBar';
import Map from '../../components/MapsComponents/Map/Map'
import styles from './Main.module.scss';

interface MainProps {
    isAuthent: boolean;
    handleLogin: () => void;
}

const Main: React.FC<MainProps> = ({ isAuthent, handleLogin }) => {
    const [selectedMarker, setSelectedMarker] = useState(null);

    return (
        <div className={styles.mainContainer}>
            <div className={styles.leftBarContainer}>
                <LeftBar isAuthent={isAuthent} handleLogin={handleLogin} setSelectedMarker={setSelectedMarker} selectedMarker={selectedMarker} /> </div>
            <div className={styles.mapContainer}>
                <Map selectedMarker={selectedMarker} setSelectedMarker={setSelectedMarker} /></div>
        </div>
    );
};

export default Main;
