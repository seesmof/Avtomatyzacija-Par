import wmi

w = wmi.WMI()
kodi_process = w.Win32_Process(name='kodi.exe')

if kodi_process:
    print('Kodi is running!')
