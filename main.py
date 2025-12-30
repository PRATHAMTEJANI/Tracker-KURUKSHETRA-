from pynput import mouse, keyboard
import time
from datetime import datetime
from analyzer import analyze_window
from storage import save_session
from plyer import notification
import ctypes
import psutil

# ---------------- CONFIG ----------------
WINDOW_DURATION = 60          # ✅ 1 minute window
DRIFT_WARNING_LIMIT = 5       # ✅ 5 consecutive bad minutes

# ---------------- GLOBAL STATE ----------------
mouse_moves = 0
key_presses = 0
last_activity = time.time()

drift_streak = 0

last_app = None
last_app_switch_time = time.time()
app_usage = {}   # app_name -> seconds


# ---------------- WINDOWS ACTIVE APP ----------------
def get_active_app():
    user32 = ctypes.windll.user32
    hwnd = user32.GetForegroundWindow()
    pid = ctypes.c_ulong()
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))

    try:
        return psutil.Process(pid.value).name()
    except:
        return "Unknown"


# ---------------- WARN USER ----------------
def warn_user(state):
    notification.notify(
        title="⚠️ Cognitive Drift Detected",
        message=f"Unnecessary activity detected: {state}",
        timeout=5
    )


# ---------------- INPUT LISTENERS ----------------
def on_move(x, y):
    global mouse_moves, last_activity
    mouse_moves += 1
    last_activity = time.time()


def on_press(key):
    global key_presses, last_activity
    key_presses += 1
    last_activity = time.time()


mouse.Listener(on_move=on_move).start()
keyboard.Listener(on_press=on_press).start()

print("🧠 Cognitive Drift Tracker started")
print("⏱️ Tracking focus + app usage every 1 minute...\n")


# ---------------- MAIN LOOP ----------------
while True:
    WINDOW_START = time.time()
    last_app = get_active_app()
    last_app_switch_time = WINDOW_START
    app_usage = {}

    # ⏱️ 1-minute tracking window
    while time.time() - WINDOW_START < WINDOW_DURATION:
        time.sleep(1)
        current_app = get_active_app()

        if current_app != last_app:
            duration = int(time.time() - last_app_switch_time)
            app_usage[last_app] = app_usage.get(last_app, 0) + duration

            last_app = current_app
            last_app_switch_time = time.time()

    # final app time
    duration = int(time.time() - last_app_switch_time)
    app_usage[last_app] = app_usage.get(last_app, 0) + duration

    idle_time = int(time.time() - last_activity)

    # ANALYZE COGNITIVE STATE
    state, score = analyze_window(
        mouse_moves,
        key_presses,
        len(app_usage),
        idle_time
    )

    if state in ["Mind Drift", "Fake Productivity"]:
        drift_streak += 1
    else:
        drift_streak = 0

    if drift_streak >= DRIFT_WARNING_LIMIT:
        warn_user(state)
        print("⚠️ WARNING: Unnecessary activity detected")
        drift_streak = 0


    session = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "focus_state": state,
        "focus_score": score,
        "mouse_moves": mouse_moves,
        "key_presses": key_presses,
        "idle_seconds": idle_time,
        "app_usage_seconds": app_usage
    }

    save_session(session)

    print(f"[{session['timestamp']}] {state} | Score: {score}")
    print("App usage (seconds):", app_usage)
    print("-" * 50)

    mouse_moves = 0
    key_presses = 0
