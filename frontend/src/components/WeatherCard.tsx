import type { Weather } from "../types/weather";

interface Props {
  weather: Weather;
}

const WeatherCard = ({ weather }: Props) => {
  return (
    <div>
      <h2>Clima Actual</h2>
      <p>Temperatura: {weather.temperature}°</p>
      <p>Condición: {weather.weather_condition}</p>
      <p>Humedad: {weather.humidity}%</p>
    </div>
  );
};

export default WeatherCard;
