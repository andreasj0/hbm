import pyautogui as pag
import webbrowser
import time
webbrowser.open("https://humanbenchmark.com/tests/aim")

time.sleep(2) # Wait for browser to open
levels = 31 # 30 levels

for i in range(levels):
    (x, y) = pag.locateCenterOnScreen('aimdot.png', confidence=0.3, region=(400, 200, 1540, 820)) # This resolution is very ish
    pag.click(x, y)