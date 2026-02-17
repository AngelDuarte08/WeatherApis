export interface Weather {
  temperature: number;
  condition: string;
  humidity: number;
  icon: string;
}

export interface ForecastHour { 
  time: string;         
  temperature: number;  
  condition: string;
  isDaytime: boolean;
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
  forecast: ForecastHour[];
  air: AirQuality;
}