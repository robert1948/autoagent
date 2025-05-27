# 🚀 AutoAgent

**AutoAgent** is an intelligent fullstack web platform built with FastAPI, React, and PostgreSQL. It provides a powerful foundation for authenticated user and developer onboarding, agent execution, and adaptive task flows — all integrated with modern AI capabilities.

---

## 📦 Tech Stack

- **Backend**: FastAPI + SQLAlchemy + PostgreSQL
- **Frontend**: React + Bootstrap + AuthContext + Axios
- **Auth**: JWT (Role-based, hashed passwords)
- **Deployment**: Heroku (via GitHub integration)
- **CI/CD**: Manual + Auto-deploy from GitHub main branch

---

## 📌 Features

- ✅ User & Developer registration/login
- ✅ JWT-based authentication with protected routes
- ✅ Role-based profile handling via `/me`
- ✅ React frontend with live auth status
- ✅ Heroku deployment: backend + static React frontend
- ✅ Swagger API with pre-filled dev JWT for testing
- ✅ Onboarding agent scaffold in progress

---

## 📁 Project Structure

```
autoagent/
├── backend/        # FastAPI backend
│   └── src/        # Main app logic
│       ├── routes, schemas, models, auth, etc.
├── client/         # React frontend
│   └── src/        # Pages, components, services
├── scripts/        # Utilities & deployment helpers
├── static/         # Contains built React app (for Heroku)
├── .env            # Local environment variables
├── Procfile        # Heroku entry point
├── requirements.txt
└── ROADMAP.md      # Development milestones and progress
```

---

## 🧪 Local Development

1. **Install backend requirements**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Start backend**  
   ```bash
   cd backend
   uvicorn src.main:app --reload --port 8000
   ```

3. **Start frontend**  
   ```bash
   cd client
   npm install
   npm start
   ```

4. Visit:
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🚀 Production Deployment

Auto-deploys to Heroku:
- 🌍 [https://autorisen-d2ba5f0027e2.herokuapp.com](https://autorisen-d2ba5f0027e2.herokuapp.com)

Steps:
1. `npm run build` in `client/`
2. Copy to `backend/static/`
3. Push to GitHub → triggers Heroku build

---

## 📅 Development Roadmap

See [ROADMAP.md](./ROADMAP.md) for milestone breakdowns:
- Project Setup
- Auth System
- Frontend Integration
- Heroku Deployment
- Onboarding Flow
- Agent Execution
- UI Polish

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome!

---

## 📜 License

MIT License © 2025 Robert1948