import pyautogui
import pydirectinput
import time

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

# pyautogui.moveTo(375,139) # Move the mouse to XY coordinates.

# pyautogui.click(270,124)          # Click the mouse.
# pyautogui.rightClick(434,102)  # Move the mouse to XY coordinates and click it.
# pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
time.sleep(4)

pydirectinput.rightClick(362,251)

# pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
# pyautogui.doubleClick()     # Double click the mouse.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

# # pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# # pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

# # with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
# #         pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# # # Shift key is released automatically.

# # pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

# pyautogui.alert('This is the message to display.') # Make an alert b