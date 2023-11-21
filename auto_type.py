import pyautogui
from time import sleep
sleep(3)
for i in range(0,4):
    pyautogui.write('Hello world!', interval=0.25)
    # pyautogui.press('enter')