import React, { useEffect, useState } from 'react';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import defaultImg from 'leaflet/dist/images/marker-icon.png';
import selectedImg from '../../../assets/logo.svg';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';
import styles from './Map.module.scss';

interface MapProps {
    selectedMarker: any,
    setSelectedMarker: any,

}

const Map = ({ selectedMarker, setSelectedMarker }: MapProps) => {
    const position1 = [51.505, -0.09];
    const position2 = [51.51, -0.1];
    const position3 = [51.5075, -0.095];

    const defaultIcon = L.icon({
        iconAnchor: [12, 41],
        iconSize: [25, 41],
        iconUrl: defaultImg,
        popupAnchor: [1, -34],
        shadowSize: [41, 41],
        shadowUrl: iconShadow,
    });

    const selectedIcon = L.icon({
        iconAnchor: [12, 41],
        iconSize: [25, 41],
        iconUrl: selectedImg,
        popupAnchor: [1, -34],
        shadowSize: [41, 41],
        shadowUrl: iconShadow,
    });

    const [markers, setMarkers] = useState([
        { position: position1, icon: defaultIcon, id: 1 },
        { position: position2, icon: defaultIcon, id: 2 },
        { position: position3, icon: defaultIcon, id: 3 },
    ]);

    useEffect(() => {
        const map = L.map('map').setView([51.505, -0.09], 13);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        const drawnLines: L.Polyline[] = [];
        const markerInstances: { [id: number]: L.Marker } = {};

        markers.forEach(marker => {
            const markerInstance = L.marker(marker.position as L.LatLngExpression, { icon: defaultIcon, draggable: true })
                .addTo(map)
                .bindPopup(`Latitude: ${marker.position[0]}, Longitude: ${marker.position[1]}`)
                .on('click', () => {
                    setSelectedMarker(null);
                    setSelectedMarker(marker.id);
                });

            markerInstance.on('dragend', (event) => {
                const newPosition = event.target.getLatLng();
                marker.position = [newPosition.lat, newPosition.lng];
                markerInstance.setIcon(defaultIcon);

                // Update popup content with new coordinates
                markerInstance.setPopupContent(`Latitude: ${newPosition.lat}, Longitude: ${newPosition.lng}`);

                // Clear previous lines
                drawnLines.forEach(line => map.removeLayer(line));

                // Draw lines between all markers
                markers.forEach(otherMarker => {
                    if (otherMarker.id !== marker.id) {
                        const line = L.polyline([marker.position as L.LatLngExpression, otherMarker.position as L.LatLngExpression], { color: 'red' }).addTo(map);
                        drawnLines.push(line);
                        if (otherMarker.id === selectedMarker) {
                        }
                    }
                });
            });
        });
    }, [markers]);

    return <div id="map" className={styles.mapContainer} />;
};

export default Map;
