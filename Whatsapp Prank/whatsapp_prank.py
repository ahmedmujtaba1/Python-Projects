import pyautogui as pg
import time

time.sleep(5)
count = 0

while count<=10:
    pg.typewrite('Hello Its me Ahmed !')
    pg.press("Enter")
    count += 1
