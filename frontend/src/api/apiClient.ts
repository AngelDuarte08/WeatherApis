import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000/api', 
  headers: {
    'Content-Type': 'application/json',
  }
});

export const weatherAPI = {
  getLocation: async (ciudad: string) => {
    // Todos usan la llave "ciudad" ahora
    const response = await api.post('/location', { ciudad });
    return response.data;
  },

  getCurrentWeather: async (ciudad: string) => {
    const response = await api.post('/current-weather', { ciudad });
    return response.data;
  },

  getForecast: async (ciudad: string) => {
    const response = await api.post('/forecast', { ciudad });
    return response.data;
  },

  getAirQuality: async (ciudad: string) => {
    const response = await api.post('/air-quality', { ciudad });
    return response.data;
  }
};