import type { Weather } from "../types/weather";

interface Props {
  weather: Weather;
}

const WeatherCard = ({ weather }: Props) => {
  return (
    <div style={{ textAlign: 'center' }}>
      <h2>Clima Actual</h2>
      {/* Añadimos .png al final si la URL viene incompleta */}
      <img 
        src={`${weather.icon}.png`} 
        alt={weather.condition} 
        style={{ width: '64px' }} 
      />
      <p>Temperatura: {weather.temperature}°C</p>
      <p>Condición: {weather.condition}</p>
      <p>Humedad: {weather.humidity}%</p>
    </div>
  );
};

export default WeatherCard;