import pandas as pd
from datetime import date

FILE = "data/progress.csv"

def log_progress(subject, chapter, status):
    today = date.today().isoformat()

    row = pd.DataFrame([{
        "date": today,
        "subject": subject,
        "chapter": chapter,
        "status": status
    }])

    try:
        old = pd.read_csv(FILE)
        new = pd.concat([old, row], ignore_index=True)
    except:
        new = row

    new.to_csv(FILE, index=False)

