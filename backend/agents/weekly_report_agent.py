import pandas as pd

def generate_weekly_report():
    try:
        df = pd.read_csv("data/progress.csv")

        completed = df[df["status"] == "Completed"]
        skipped = df[df["status"] == "Skipped"]

        completed_counts = completed["subject"].value_counts()
        skipped_counts = skipped["subject"].value_counts()

        report = {}

        for subject in df["subject"].unique():
            report[subject] = {
                "completed": int(completed_counts.get(subject, 0)),
                "skipped": int(skipped_counts.get(subject, 0))
            }

        return report
    except:
        return {}
