def analyze_window(mouse_moves, key_presses, app_switches, idle_time):
    score = 100

    if idle_time > 300:
        score -= 40

    if app_switches > 15:
        score -= 30

    if key_presses < 10:
        score -= 20

    if mouse_moves < 20:
        score -= 10

    if score >= 70:
        state = "Focused Work"
    elif score >= 40:
        state = "Fake Productivity"
    else:
        state = "Mind Drift"

    return state, max(score, 0)
