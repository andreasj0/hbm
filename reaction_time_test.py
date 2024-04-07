import pyautogui as pag
import webbrowser
import time
webbrowser.open("https://humanbenchmark.com/tests/reactiontime")

time.sleep(2)

levels = 5
green_color = (79, 219, 110) # RGB
blue_color = (55, 135, 207) # # RGB

offset_value = 50 # Makes sure that the cursor lands on background color and not white text
(screen_width, screen_height) = pag.size()
box_width = int(screen_width / 2)
box_height = int(screen_height / 2) + offset_value
pag.moveTo(box_width, box_height)



    

for i in range(levels): # 5 levels in total
    color = pag.pixel(box_width, box_height)

    if color == blue_color: 
        pag.click() # Clicks if color is blue

    while color != green_color:
        color = pag.pixel(box_width, box_height)
        
    pag.click() # Clicks if color is green
        