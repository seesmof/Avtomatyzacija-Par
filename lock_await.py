from library import *


def on_keystroke():
    webbrowser.open("https://youtu.be/MVPTGNGiI-4")

    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        volume.SetMasterVolume(0.4, None)

    time.sleep(3)

    ctypes.windll.user32.LockWorkStation()


keyboard.add_hotkey("ctrl+shift+'", on_keystroke)
print("Waiting for hotkey")
keyboard.wait()
