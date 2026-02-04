import pandas as pd
from datetime import date, timedelta

def get_revision_tasks():
    try:
        df = pd.read_csv("data/progress.csv")
        df["date"] = pd.to_datetime(df["date"])

        target_day = date.today() - timedelta(days=2)

        revision = df[df["date"] == str(target_day)]
        return revision[["subject","chapter"]]

    except:
        return None
