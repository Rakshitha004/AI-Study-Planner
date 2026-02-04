from agents.difficulty_agents import get_dynamic_difficulty

def identify_weak_subjects(results_df):
    weak = results_df[results_df["Marks"] < 70]["Subject"].tolist()
    return weak


def generate_daily_plan(chapters_df, weak_subjects, max_hours):
    plan = []
    sessions = max_hours * 2

    for _, row in chapters_df.iterrows():
        subject = row["Subject"]
        chapter = row["Chapter_Name"]

        priority = get_dynamic_difficulty(chapter)

        plan.append(f"{subject} → {chapter} ({priority})")

        if len(plan) >= sessions:
            break

    return plan



