# 🌍 Air Location Intelligence App

A full-stack web application that allows users to enter a location and visualize real-time environmental information, including:

- 📍 Interactive map with coordinates
- 🌫️ Air quality data
- 🌡️ Current weather conditions
- 📅 Weather forecast
- 📲 Send and receive information via SMS using Twilio

The system uses **React** for the frontend and **Flask** for the backend, integrating **Google APIs** and **Twilio services**.

---

## 🧱 Project Architecture

```
React (Frontend)
      ↓
Flask API (Backend)
      ↓
Google APIs / Twilio
```

---

## ⚙️ Technologies Used

### Frontend

- React
- Axios / Fetch API
- Google Maps JavaScript API
- CSS / Tailwind (optional)

### Backend

- Flask
- Flask-CORS
- Requests
- Python-dotenv

### External Services

- Google Maps Platform
- Google Air Quality API
- Google Weather API (or weather provider)
- Twilio SMS API

---

## 📁 Project Structure

```
air-location-app/
│
├── frontend/                 # React application
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   ├── package.json
│   └── .env
│
├── backend/                  # Flask API
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── models/
│   │   └── utils/
│   ├── run.py
│   ├── requirements.txt
│   └── .env
│
├── docs/
├── README.md
└── .gitignore
```

---

## 🔐 Environment Variables

Create a `.env` file inside the `backend/` directory:

```
GOOGLE_MAPS_API_KEY=
GOOGLE_WEATHER_API_KEY=
GOOGLE_AIR_API_KEY=

TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=
```

---

## 🚀 Installation and Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/AngelDuarte08/WeatherApis.git
cd WeatherAPisFull
```

---

### 2️⃣ Backend (Flask)

```
cd backend
python -m venv venv
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
python run.py
```

Server runs at:

```
http://localhost:5000
```

---

### 3️⃣ Frontend (React)

```
cd frontend
npm install
npm run dev
```

Application runs at:

```
http://localhost:5173
```

---

## 📡 API Endpoints

| Method | Endpoint                | Description                  |
| ------ | ----------------------- | ---------------------------- |
| POST   | `/api/location`         | Get coordinates from address |
| GET    | `/api/weather/current`  | Current weather              |
| GET    | `/api/weather/forecast` | Weather forecast             |
| GET    | `/api/air-quality`      | Air quality data             |
| POST   | `/api/send-sms`         | Send SMS message             |
| POST   | `/api/twilio-webhook`   | Receive SMS response         |

---

## 📲 Application Flow

1. User enters a location.
2. React sends a request to the backend.
3. Flask queries Google APIs.
4. The system returns:
   - Coordinates
   - Interactive map
   - Air quality data
   - Current weather
   - Forecast

5. User can request information via SMS.
6. Twilio sends responses to a Flask webhook.

---

## 🧠 Main Features

✔ Accurate geolocation
✔ Interactive map visualization
✔ Real-time environmental data
✔ Weather forecasting
✔ Bidirectional SMS integration
✔ Modular and scalable architecture

---

## 🔮 Future Improvements

- Location search history
- User authentication
- Automatic air quality alerts
- Analytics dashboard
- Push notifications
- Cloud deployment
- Docker containerization

---

## 🧪 Testing (optional)

```
pytest
```

---

## ☁️ Recommended Deployment

Frontend:

- Vercel
- Netlify

Backend:

- Render
- Railway
- AWS

---

## 👨‍💻 Author

Developed by: **Angel Duarte**

---

## 📜 License

MIT License
