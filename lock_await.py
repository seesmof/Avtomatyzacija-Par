from library import *

from pynput import keyboard
import webbrowser
import win32gui
import win32con


def on_press(key):
    if key == keyboard.Key.ctrl_l and keyboard.Key.shift_l and key.char == "'":
        webbrowser.open("https://youtu.be/MVPTGNGiI-4")
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)


listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
