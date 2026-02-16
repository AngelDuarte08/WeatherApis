import type{ AirQuality } from "../types/weather";

interface Props {
  air: AirQuality;
}

const AirQualityCard = ({ air }: Props) => {
  return (
    <div>
      <h2>Calidad del Aire</h2>
      <p>AQI: {air.aqi}</p>
      <p>Categoría: {air.category}</p>
    </div>
  );
};

export default AirQualityCard;
