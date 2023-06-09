import keyboard
import webbrowser
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import time
import ctypes


def on_keystroke():
    webbrowser.open("https://youtu.be/MVPTGNGiI-4")

    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(0.15, None)

    time.sleep(3)

    ctypes.windll.user32.LockWorkStation()


keyboard.add_hotkey("ctrl+shift+'", on_keystroke)
keyboard.wait()
