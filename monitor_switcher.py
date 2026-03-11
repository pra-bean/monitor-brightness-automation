import os
from datetime import datetime
from win10toast import ToastNotifier

MODE_TRACK_FILE = "last_mode.txt"
CLICKMONITOR_PATH = r"C:\Softwares\ClickMonitorDDC_7_2\ClickMonitorDDC_7_2.exe"

DAY_MODE = (40, 60)
NIGHT_MODE = (10, 40)

notifier = ToastNotifier()

def set_monitor_settings(brightness, contrast):
    os.system(f'"{CLICKMONITOR_PATH}" b {brightness}')
    os.system(f'"{CLICKMONITOR_PATH}" c {contrast}')

def show_notification(title, message):
    notifier.show_toast(title, message, duration=5, threaded=True)

def get_last_mode():
    if not os.path.exists(MODE_TRACK_FILE):
        return None
    with open(MODE_TRACK_FILE, 'r') as f:
        return f.read().strip()

def save_current_mode(mode):
    with open(MODE_TRACK_FILE, 'w') as f:
        f.write(mode)

def main():
    hour = datetime.now().hour
    last_mode = get_last_mode()

    if 8 <= hour < 18:
        current_mode = "day"
        if last_mode != current_mode:
            set_monitor_settings(*DAY_MODE)
            show_notification("Day Mode Activated", "Brightness and contrast set for daytime.")
            save_current_mode(current_mode)
    else:
        current_mode = "night"
        if last_mode != current_mode:
            set_monitor_settings(*NIGHT_MODE)
            show_notification("Night Mode Activated", "Settings switched to night mode.")
            save_current_mode(current_mode)

    with open("C:\\monitor_log.txt", "a") as log:
        log.write(f"{datetime.now()} - Script ran.\n")

if __name__ == "__main__":
    main()
