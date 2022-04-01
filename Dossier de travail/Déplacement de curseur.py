import pyautogui
import random
import time
départx=random.randint(1, 1920)
départy=random.randint(1, 1080)
pyautogui.moveTo(départx, départy)

time.sleep(2)
vi=5
cox = random.randint(48, 70)
coy = random.randint(435,458)
pyautogui.moveTo(cox,coy,vi)
time.sleep(0.2)
pyautogui.click()