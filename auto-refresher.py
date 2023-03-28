# include necessary dependencies
import pyautogui
import time

# create an infinite loop
while True:
    # refresh the page
    pyautogui.press('f5')
    # wait for 10 seconds before refreshing again
    time.sleep(10)
