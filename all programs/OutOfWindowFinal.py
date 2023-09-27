import pyautogui
import time
import win32gui

mouse_within_tab = True
delay_threshold = 2  
last_cursor_move_time = time.time()

while True:

    mouse_x, mouse_y = pyautogui.position()

    active_app = win32gui.GetForegroundWindow()

    if win32gui.IsWindowVisible(active_app):
        app_left, app_top, app_right, app_bottom = win32gui.GetWindowRect(active_app)
        if (app_left <= mouse_x <= app_right and
            app_top <= mouse_y <= app_bottom):
            if not mouse_within_tab:

                print("Mouse cursor moved out the active tab.")
                mouse_within_tab = True
                last_cursor_move_time = time.time()
        else:
            if mouse_within_tab:

                current_time = time.time()
                cursor_move_delay = current_time - last_cursor_move_time
                if cursor_move_delay >= delay_threshold:

                    print("Mouse cursor moved out of the active tab.")

                    with open('event_log.txt', 'a') as file:
                        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                        file.write(f'Mouse cursor moved out of the active tab at {timestamp}\n')

            mouse_within_tab = False

    last_cursor_move_time = time.time()

    time.sleep(0.1)