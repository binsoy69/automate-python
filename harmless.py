""" Prank someone using this script """
# using pyautogui 
# make the mouse movement out of control 
# I've made this as an april fool's joke/script
# 4/1/2021
import pyautogui, time, random

def move_mouse(sec):
  start = time.time()
  elapsed = time.time() - start
  xsize, ysize = pyautogui.size()

  while elapsed < sec:
    x, y = random.randrange(xsize), random.randrange(ysize)
    pyautogui.moveTo(x, y, duration=0.2)
    elapsed = time.time() - start

if __name__ == '__main__':
  pyautogui.FAILSAFE = True
  try:
    pyautogui.alert('Your download is now complete!')
    move_mouse(3)
    pyautogui.alert('You are hacked!! HAHAHAH')
    move_mouse(100)
  except pyautogui.FailSafeException:
    pyautogui.alert('Just kidding, You have been fooled!')