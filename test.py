import os
import time
import subprocess


def start_recording():
    # Get the current time
    now = time.strftime("%H:%M", time.localtime())

    # Set the path to your OBS executable
    obs_path = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"

    # Set the path to your OBS recording profile
    profile_path = "C:\\Users\\<username>\\AppData\\Roaming\\obs-studio\\basic\\profiles\\Untitled"

    # Set the path to the folder where you want to save your recordings
    output_folder = "C:\\Users\\<username>\\Videos"

    # Start the recording
    subprocess.call([obs_path, "--startrecording", "--minimize-to-tray", "--profile",
                    profile_path, "--output", os.path.join(output_folder, "Recording_" + now + ".mp4")])


if __name__ == "__main__":
    start_recording()
