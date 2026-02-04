import pandas as pd

def load_all_data():
    profile = pd.read_csv("data/profile.csv")
    schedule = pd.read_csv("data/schedule.csv")
    chapters = pd.read_csv("data/chapters.csv")
    exam_window = pd.read_csv("data/Exam_Window.csv")
    results = pd.read_csv("data/results.csv")

    return {
        "profile": profile,
        "schedule": schedule,
        "chapters": chapters,
        "exam_window": exam_window,
        "results": results
    }
