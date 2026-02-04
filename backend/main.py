from fastapi import FastAPI
from datetime import datetime

# create app first
app = FastAPI()

# imports
from load_data import load_all_data
from agents.planner import identify_weak_subjects, generate_daily_plan
from agents.schedule_agent import get_free_slots
from agents.revision_agent import get_revision_tasks
from agents.progress_agent import log_progress
from llm import ask_llm
from agents.tutor_agent import solve_doubt, generate_practice_questions, summarize_text
from agents.streak_agent import mark_today_study, calculate_streak
from agents.weekly_report_agent import generate_weekly_report
from agents.flashcard_agent import generate_flashcards
from agents.mocktest_agent import generate_mock_test
from agents.pomodoro_agent import start_pomodoro, stop_pomodoro
from agents.mindmap_agent import generate_mindmap
from agents.dashboard_agent import generate_dashboard
from agents.badge_agent import get_badge


# -----------------------------
# STUDY PLAN ENDPOINT
# -----------------------------

@app.get("/generate_plan")
def generate_plan():

    data = load_all_data()

    weak_subjects = identify_weak_subjects(data["results"])
    max_hours = int(data["profile"]["max_study_hours"][0])

    tasks = generate_daily_plan(
        data["chapters"],
        weak_subjects,
        max_hours
    )

    free_slots = get_free_slots(data["schedule"])

    today = datetime.now()
    day_name = today.strftime("%A")
    date_str = today.strftime("%d %B %Y")

    plan_output = []

    for task, slot in zip(tasks, free_slots):
        plan_output.append(f"{slot} → {task}")

    revision = get_revision_tasks()

    return {
        "day": day_name,
        "date": date_str,
        "plan": plan_output,
        "revision": None if revision is None else revision.to_dict()
    }


# -----------------------------
# TUTOR ENDPOINTS
# -----------------------------

@app.get("/doubt")
def doubt(q: str):
    return {"answer": solve_doubt(q)}

@app.get("/practice")
def practice(topic: str):
    return {"questions": generate_practice_questions(topic)}

@app.post("/summary")
def summary(payload: dict):
    return {"summary": summarize_text(payload["text"])}

@app.post("/log_progress")
def log_user_progress(payload: dict):

    subject = payload["subject"]
    chapter = payload["chapter"]
    status = payload["status"]

    log_progress(subject, chapter, status)

    # if at least one task completed today → studied = True
    studied = True if status == "Completed" else False
    mark_today_study(studied)

    return {
        "message": "Saved",
        "current_streak": calculate_streak()
    }

@app.get("/weekly_report")
def weekly_report():
    return {"report": generate_weekly_report()}

@app.get("/flashcards")
def flashcards(topic: str):
    cards = generate_flashcards(topic)
    return {"topic": topic, "flashcards": cards}

@app.get("/mocktest")
def mocktest(topic: str):
    return {"topic": topic, "mcqs": generate_mock_test(topic)}

@app.get("/start_pomodoro")
def start_timer(minutes: int = 25):
    return {"message": start_pomodoro(minutes)}

@app.get("/stop_pomodoro")
def stop_timer():
    return {"message": stop_pomodoro()}

@app.get("/mindmap")
def get_mindmap(topic: str):
    return {
        "topic": topic,
        "mindmap": generate_mindmap(topic)
    }

@app.get("/dashboard")
def dashboard():
    return {"dashboard": generate_dashboard()}  

@app.get("/badge")
def badge():
    return {"badge": get_badge()}