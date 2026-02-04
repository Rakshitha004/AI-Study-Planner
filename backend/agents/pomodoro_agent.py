import time

pomodoro_start_time = None
pomodoro_duration = None

def start_pomodoro(minutes: int):
    global pomodoro_start_time, pomodoro_duration
    pomodoro_start_time = time.time()
    pomodoro_duration = minutes * 60
    return f"Pomodoro started for {minutes} minutes"

def stop_pomodoro():
    global pomodoro_start_time, pomodoro_duration

    if pomodoro_start_time is None:
        return "No active pomodoro session"

    elapsed = time.time() - pomodoro_start_time
    pomodoro_start_time = None
    pomodoro_duration = None

    return f"Session ended. You focused for {int(elapsed/60)} minutes"
