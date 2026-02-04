import pandas as pd
from datetime import date

FILE = "data/streaks.csv"

def mark_today_study(studied: bool):
    today = date.today().isoformat()
    row = pd.DataFrame([[today, "yes" if studied else "no"]],
                       columns=["date","studied"])

    try:
        old = pd.read_csv(FILE)
        row = pd.concat([old,row])
    except:
        pass

    row.to_csv(FILE, index=False)


def calculate_streak():
    try:
        df = pd.read_csv(FILE)
        streak = 0

        for value in reversed(df["studied"].tolist()):
            if value == "yes":
                streak += 1
            else:
                break

        return streak
    except:
        return 0
