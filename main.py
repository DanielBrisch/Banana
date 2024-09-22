import pygetwindow as gw
import pyautogui
import keyboard  

window_title = "Banana"
window = gw.getWindowsWithTitle(window_title)

burger_window = window[0]

burger_window.activate()

center_x = burger_window.left + burger_window.width // 2
center_y = burger_window.top + burger_window.height // 1.70

while True:
    if keyboard.is_pressed('esc'):  
        break
    pyautogui.click(center_x, center_y)