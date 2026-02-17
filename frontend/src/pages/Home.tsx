import { useState } from 'react';
import { weatherAPI } from '../api/apiClient';
import type { FullData } from '../types/weather';

import SearchForm from '../components/SearchForm';
import WeatherCard from '../components/WeatherCard';
import ForecastCard from '../components/ForecastCard';
import AirQualityCard from '../components/AirQualityCard';
import MapEmbed from '../components/MapEmbed';

const Home = () => {
  const [climaData, setClimaData] = useState<FullData | null>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleSearch = async (ciudad: string) => {
    setLoading(true);
    try {
      const weatherRes = await weatherAPI.getCurrentWeather(ciudad);
      const forecastRes = await weatherAPI.getForecast(ciudad);
      const airRes = await weatherAPI.getAirQuality(ciudad);

      setClimaData({
      ciudad: weatherRes.ciudad,
      lat: weatherRes.lat,
      lng: weatherRes.lng,
      weather: {
        temperature: weatherRes.weather.temperature.degrees,
        condition: weatherRes.weather.weather_condition.description.text,
        humidity: weatherRes.weather.humidity || 0,
        icon: weatherRes.weather.weather_condition.iconBaseUri
      },
      // Aquí pasamos el array de horas directamente
      forecast: forecastRes.forecast, 
      air: airRes.air_quality
    });

    } catch (err) {
      console.error("Error al procesar datos:", err);
      alert("Error al procesar la información del servidor.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container" style={{ padding: '20px' }}>
      <h1>Weather App</h1>
      <SearchForm onSearch={handleSearch} />

      {loading && <p>Cargando información...</p>}

      {climaData && !loading && (
        <div className="results-grid" style={{ marginTop: '20px' }}>
          <WeatherCard weather={climaData.weather} />
          <AirQualityCard air={climaData.air} />
          <ForecastCard forecast={climaData.forecast} />
          <MapEmbed lat={climaData.lat} lng={climaData.lng} />
        </div>
      )}
    </div>
  );
};

export default Home;