import pandas as pd

PROGRESS_FILE = "data/progress.csv"
CHAPTERS_FILE = "data/chapters.csv"

def generate_dashboard():
    progress = pd.read_csv(PROGRESS_FILE)
    chapters = pd.read_csv(CHAPTERS_FILE)

    result = {}

    for subject in chapters["Subject"].unique():
        total = len(chapters[chapters["Subject"] == subject])
        done = len(
            progress[
                (progress["subject"] == subject) &
                (progress["status"] == "Completed")
            ]
        )

        percent = 0 if total == 0 else round((done / total) * 100, 2)

        result[subject] = {
            "completed": done,
            "total": total,
            "percentage": percent
        }

    return result
