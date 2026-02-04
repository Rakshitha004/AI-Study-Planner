import pandas as pd

def get_dynamic_difficulty(chapter):

    try:
        df = pd.read_csv("data/progress.csv")
        chapter_df = df[df["chapter"] == chapter]

        skipped = len(chapter_df[chapter_df["status"] == "Skipped"])
        completed = len(chapter_df[chapter_df["status"] == "Completed"])

        if skipped >= 2:
            return "Focus"
        elif completed >= 2:
            return "Quick Review"
        else:
            return "Practice"
    except:
        return "Practice"
