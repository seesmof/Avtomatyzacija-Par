from library import *


def monitor_kodi():
    w = wmi.WMI()
    while True:
        kodi_process = w.Win32_Process(name='kodi.exe')
        if kodi_process:
            rating_system()
            letterbox_lists()
            while kodi_process:
                time.sleep(1)
                kodi_process = w.Win32_Process(name='kodi.exe')
        time.sleep(1)


monitor_kodi()
