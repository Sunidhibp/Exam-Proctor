import psutil
import time
import pygetwindow as gw

def is_process_running(process_name):
    for process in psutil.process_iter(attrs=['name']):
        try:
            if process.info['name'] == process_name:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def is_window_open(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    return len(windows) > 0

def monitor_background_processes():
    prohibited_apps = [
        {"name": "Calculator", "process_name": "calc.exe"},
        {"name": "Chrome", "process_name": "chrome.exe"},
        {"name": "Edge", "process_name": "edge.exe"},
        {"name": "Brave", "process_name": "brave.exe"},
        {"name": "OneNote", "process_name": "onenote.exe"}

    ]

    while True:
        for app in prohibited_apps:
            if is_process_running(app["process_name"]) or is_window_open(app["name"]):
                print(f"Prohibited app detected: {app['name']}")
        
        time.sleep(5)  # Check for prohibited apps every 5 seconds

if __name__ == "__main__":
    monitor_background_processes()