# AI Study Planner 🧠📚

An AI-powered study assistant that creates personalized study plans, tracks progress, generates flashcards, runs pomodoro sessions, and provides weekly performance reports.

This project is designed for students who want structured daily planning, revision tracking, and smart learning assistance.

---

## 🚀 Features

- ✅ Personalized Daily Study Plan Generator  
- 📅 Day & Date based scheduling  
- 📊 Weak subject identification  
- 🔁 Revision task generator  
- 🧠 AI Flashcard Generator (topic based)  
- ⏱ Pomodoro Timer  
- 📈 Study Streak Tracking  
- 📝 Progress Logging (Completed / Skipped)  
- 📊 Weekly Study Report  

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Pandas
- CSV-based storage
- LLM integration (Ollama / Local LLM)

### Frontend(In Progress)
- React (Vite)
- Tailwind CSS

---

## 📂 Project Structure

study_coach_ai/
│
├── backend/
│ ├── agents/
│ ├── data/
│ ├── main.py
│ ├── load_data.py
│ └── llm.py
│
├── frontend/
│ └── (React App)
│
└── README.md

## ▶️ How To Run Backend

cd backend
pip install fastapi uvicorn pandas
python -m uvicorn main:app --reload


Open:

http://127.0.0.1:8000/docs


---

## ▶️ How To Run Frontend

cd frontend
npm install
npm run dev


---

## 🧪 Example APIs

- GET /generate_plan  
- POST /log_progress  
- GET /flashcards?topic=Pollution  
- GET /weekly_report  

---

## 🎯 Future Enhancements

- User Authentication  
- Cloud Database  
- Mobile App  
- AI Mindmap Generator  
- Dark / Light Theme  

---

## 👩‍💻 Author

Rakshitha PR  