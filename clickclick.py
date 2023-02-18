import pyautogui
import time
import random
import subprocess

def start_clicking():
    # Define the time interval for clicking in seconds
    click_interval = 10

    # Generate random positions to click at
    screen_width, screen_height = pyautogui.size()
    positions = [(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(3)]

    # Loop through the positions and click every `click_interval` seconds
    try:
        while True:
            for position in positions:
                pyautogui.click(position[0], position[1])
                time.sleep(click_interval)
                
            subprocess.run("cmd /c start cmd /c ping google.com", shell=True)
            time.sleep(20)
    except KeyboardInterrupt:
        print("Autoclicking stopped.")

start_clicking()
