'''
Thanks to
https://m.habr.com/ru/post/533640/
https://pyautogui.readthedocs.io/en/latest/
https://github.com/eternnoir/pyTelegramBotAPI

To prevent locking of the main PC open https://www.youtube.com/watch?v=I3ZbzWomdUU
Then switch to WS
'''
import sys
from random import random, randint
import time
from time import sleep
import pyautogui
# import pywinauto
# import win32gui
# import os
# import sys

# def openNotepad():
#     osCommandString = "notepad.exe file01.txt"
#     os.system(osCommandString)

# def windowEnumerationHandler(hwnd, top_windows):
#     top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

# *********************************************
#ROUND_DURATION_TO_MOVE_MOUSE = 1
#ROUND_DURATION_TO_MOVE_MOUSE = 6
DEF_SYS_ENV_HOW_LONG_TO_WORK = 60*60*8
DEF_SYS_ENV_PERIOD_BETWEEN_DRAGGING = 300
ROUND_SLEEP_TIMEOUT_INCREMENTAL = 1
COORDINATES_THRESHOLD_FOR_CHECK_WHILE_SLEEPING = 100

#sys.argv contains arguments which are input in the terminal.
# print ('Number of arguments:',len(sys.argv))

# Arguments are printed as a list
# print ('Arguments:', str(sys.argv))

if (len(sys.argv) == 1):
    print("Use arguments 'python App.py 28800 300' for working 8 hr with delays 5 min.")
    print("DEFAULT PARAMETERS ARE USED: Working [" + str(DEF_SYS_ENV_HOW_LONG_TO_WORK) + "] with delays [" + str(DEF_SYS_ENV_PERIOD_BETWEEN_DRAGGING) + "]")

if (len(sys.argv) > 1):
    DEF_SYS_ENV_HOW_LONG_TO_WORK = int(sys.argv[1])

if (len(sys.argv) > 2):
    DEF_SYS_ENV_PERIOD_BETWEEN_DRAGGING = int(sys.argv[2])

print("PARAMETERS: Working [" + str(DEF_SYS_ENV_HOW_LONG_TO_WORK) + "] with delays [" + str(DEF_SYS_ENV_PERIOD_BETWEEN_DRAGGING) + "]")
ROUND_SLEEP_TIMEOUT = DEF_SYS_ENV_PERIOD_BETWEEN_DRAGGING #10
MAX_DURATION = DEF_SYS_ENV_HOW_LONG_TO_WORK #60*60 #60*60*2
MAX_TIME_TO_MOVE_CURSOR = 10


screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
print("Primary Screen size: W [" + str(screenWidth) + "], H[" + str(screenHeight) + "]")

currentTime = time.time()
maxTime = currentTime + MAX_DURATION

# print("Start time in s = " + str(currentTime))
print("Start time: ", time.ctime(currentTime))
# print("Stop time in s = " + str(maxTime))
print("Stop time: ", time.ctime(maxTime))





try:
    while currentTime < maxTime:
        currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.
        # print("Current position: X [" + str(currentMouseX) + "], Y[ " + str(currentMouseY) + "]")

        randX = randint(10, screenWidth-10)
        randY = randint(10, screenHeight-10)
        randTimeToMove = randint(1, MAX_TIME_TO_MOVE_CURSOR)
        # print("Target position: X [" + str(randX) + "], Y[" + str(randY) + "]")
        # print("Moving in " + str(randTimeToMove) + "s")

        pyautogui.moveTo(randX, randY, randTimeToMove)

        currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
        # print("Now in position: X [" + str(currentMouseX) + "], Y[" + str(currentMouseY) + "]")

        currentTime = time.time()
        # print("CurrentTime in s = " + str(currentTime))
        # print("CurrentTime time: ", time.ctime(currentTime))

        timeLeftToExit = maxTime - currentTime
        print("Seconds left to normal exit = " + str(timeLeftToExit).split('.')[0])
        for i in range(ROUND_SLEEP_TIMEOUT):
            sleep(ROUND_SLEEP_TIMEOUT_INCREMENTAL)
            oldMouseX, oldMouseY = currentMouseX, currentMouseY
            currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.
            if (abs(oldMouseX - currentMouseX)  > COORDINATES_THRESHOLD_FOR_CHECK_WHILE_SLEEPING)\
                or (abs(oldMouseY - currentMouseY)  > COORDINATES_THRESHOLD_FOR_CHECK_WHILE_SLEEPING):
                print("Move detected - Now in position: X [" + str(currentMouseX) + "], Y[" + str(currentMouseY) + "]")
                print("Left to sleep " + str(ROUND_SLEEP_TIMEOUT - i) + "s before the next round. To stop program move cursor to any corner and wait for exiting!")
                print("Corners coordinates are: [0, 0], [0, " + str(screenHeight) + "-1], [" + str(screenWidth) + "-1, 0], [" + str(screenWidth) + "-1, " + str(screenHeight) + "-1]")
            if (currentMouseX == 0 and currentMouseY == 0)\
                or (currentMouseX == screenWidth-1 and currentMouseY == 0)\
                or (currentMouseX == 0 and currentMouseY == screenHeight-1)\
                or (currentMouseX == screenWidth-1 and currentMouseY == screenHeight):
                print("Request to stop while sleeping - stopping app")
                sys. exit()

except pyautogui.FailSafeException as e:
    print("FailSafeException raised - stopping app")
    currentMouseX, currentMouseY = pyautogui.position()  # Get the XY position of the mouse.
    print("Last position: X [" + str(currentMouseX) + "], Y[" + str(currentMouseY) + "]")
    sys. exit()

print("Normal exit after [" + str(MAX_DURATION) + "s]")
