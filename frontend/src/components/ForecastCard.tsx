import type { ForecastHour } from "../types/weather"; // Asegúrate de cambiar el nombre en tu archivo types

interface Props {
  forecast: ForecastHour[];
}

const ForecastCard = ({ forecast }: Props) => {
  return (
    <div>
      <h2>Pronóstico por Horas</h2>
      <div style={{ display: 'flex', overflowX: 'auto', gap: '10px' }}>
        {forecast.map((hour, index) => (
          <div key={index} style={{ border: '1px solid #ccc', padding: '10px' }}>
            <p>{hour.time.split(' ')[1]}</p> {/* Muestra solo la hora */}
            <p>{hour.temperature}°C</p>
            <p>{hour.condition}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ForecastCard;