from agents.streak_agent import calculate_streak

def get_badge():
    streak = calculate_streak()

    if streak >= 30:
        return "Diamond"
    elif streak >= 14:
        return "Gold"
    elif streak >= 7:
        return "Silver"
    elif streak >= 3:
        return "Bronze"
    else:
        return "Starter"
