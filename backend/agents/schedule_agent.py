def get_free_slots(schedule_df):
    free_rows = schedule_df[schedule_df["Activity"] == "Free"]
    slots = []

    for _, row in free_rows.iterrows():
        slots.append(f'{row["Start_Time"]} - {row["End_Time"]}')

    return slots
