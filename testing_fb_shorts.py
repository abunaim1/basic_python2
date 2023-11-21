import random
import pyautogui as pg
from time import sleep
animal = ['Sweet', 'Lovely', 'Pakhita']
sleep(5)
for i in range(30):
    a = random.choice(animal)
    pg.write('You are my'+a)
    pg.press('enter')