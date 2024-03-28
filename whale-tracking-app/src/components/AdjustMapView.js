import { useMap, useMapEvents } from 'react-leaflet';
import { useEffect } from 'react';

const AdjustMapView = ({ route }) => {
  const map = useMap();

  useEffect(() => {
    if (route && route.length > 0) {
      const bounds = route.map(([lat, lng]) => [lat, lng]);
      map.fitBounds(bounds);
    }
  }, [route, map]);

  return null;
};
