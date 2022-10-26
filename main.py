import time
import pyautogui

def unblock():
  time.sleep(.5)
  location1 = pyautogui.locateOnScreen('1.PNG')
  time.sleep(.2)
  pyautogui.click(location1)
  location2 = pyautogui.locateOnScreen('2.PNG')
  time.sleep(.2)
  pyautogui.click(location2)
  
while (True):
  unblock()
  
print('Script done.')