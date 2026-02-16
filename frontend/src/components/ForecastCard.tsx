import type { ForecastDay } from "../types/weather";

interface Props {
  forecast: ForecastDay[];
}

const ForecastCard = ({ forecast }: Props) => {
  return (
    <div>
      <h2>Pronóstico</h2>
      {forecast.map((day, index) => (
        <div key={index}>
          <p>{day.date}</p>
          <p>Max: {day.max_temp}°</p>
          <p>Min: {day.min_temp}°</p>
          <p>{day.condition}</p>
        </div>
      ))}
    </div>
  );
};

export default ForecastCard;
