import { useState } from "react";
import API from "../api/apiClient";
import SearchForm from "../components/SearchForm";
import WeatherCard from "../components/WeatherCard";
import ForecastCard from "../components/ForecastCard";
import AirQualityCard from "../components/AirQualityCard";
import MapEmbed from "../components/MapEmbed";
import type { FullData } from "../types/weather";

const Home = () => {
  const [data, setData] = useState<FullData | null>(null);

  const handleSearch = async (ciudad: string): Promise<void> => {
    try {
      const weather = await API.post("/current-weather", { ciudad });
      const forecast = await API.post("/forecast", { ciudad });
      const air = await API.post("/air-quality", { ciudad });

      setData({
        ciudad,
        lat: weather.data.lat,
        lng: weather.data.lng,
        weather: weather.data.weather,
        forecast: forecast.data.forecast,
        air: air.data.air_quality,
      });
    } catch (error) {
      console.error(error);
    }
  };

  return (
  <div className="app-container">
    <h1 className="app-title">Clima App</h1>
    <SearchForm onSearch={handleSearch} />

    {data && (
      <>
        <MapEmbed lat={data.lat} lng={data.lng} />
        <div className="card">
          <WeatherCard weather={data.weather} />
        </div>
        <div className="card">
          <ForecastCard forecast={data.forecast} />
        </div>
        <div className="card">
          <AirQualityCard air={data.air} />
        </div>
      </>
    )}
  </div>
);
};

export default Home;
