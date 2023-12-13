import pyautogui
import time
import random

while True:
    pyautogui.hotkey('ctrl', 'alt', 't')
    time.sleep(1)
    pyautogui.write('python Desktop/Blog/Code.py')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)

    # Open and read the file containing links
    with open('links.txt', 'r') as file:
        links = [link.strip() for link in file.readlines() if link.strip()]

        random_link = random.choice(links)
    

    pyautogui.write(random_link)

    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'shift', 'w')

