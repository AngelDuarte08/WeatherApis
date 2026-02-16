export interface Weather {
  temperature: number;
  weather_condition: string;
  humidity: number;
}

export interface ForecastDay {
  date: string;
  max_temp: number;
  min_temp: number;
  condition: string;
}

export interface AirQuality {
  aqi: number;
  category: string;
}

export interface FullData {
  ciudad: string;
  lat: number;
  lng: number;
  weather: Weather;
  forecast: ForecastDay[];
  air: AirQuality;
}
