#MouseClickForWelearn.py

import pyautogui
import keyboard
import time

def click_mouse():
    while True:
        pyautogui.click(x=1238, y=1496)
        time.sleep(899)
        if keyboard.is_pressed('q'):
            break

click_mouse()
