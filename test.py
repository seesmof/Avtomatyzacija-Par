import pyautogui
from pynput.keyboard import Key, Controller

# Using pyautogui module
pyautogui.press('pageup')

# Using pynput module
keyboard = Controller()
keyboard.press(Key.page_up)
keyboard.release(Key.page_up)
