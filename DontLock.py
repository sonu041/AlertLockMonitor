#! python3
# Description: Progam to alert monitor is going to be locked.
# Author: Shuvankar Sarkar
import pyautogui, sys, time
print('Press Ctrl-C to quit.')
try:
    timeToShowMsg = 299 #in second. <--- set after how much time alert should be visible.
    x = 0
    y = 0
    prevX = 0
    prevY = 0
    counter = 0
    while True:
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + ' Y:' + str(y).rjust(4)
        #If mouse pointer got changed, counter got reset. Else increase the counter.
        if x != prevX:
            prevX = x
            prevY = y
            counter = 0
            print('Counter Reset    ', counter,'',positionStr)
        else:
            counter = counter + 1
            print('Counter Increased', counter,'',positionStr)
            #If counter value got same as predefined time to show msg then show alert.
            if counter == timeToShowMsg:
                pyautogui.alert(text='Monitor is going to be locked. Move your Cursor.', title='Monitor is going to be locked', button='OK')
        time.sleep(1)
except KeyboardInterrupt:
    print('\n')

#TODO: Reset the counter in any keyboard stroke.
#TODO: Send auto mouse/keyboard signal in particular interval so that monitor not got locked in anytime.
#TODO: FInd the monitor lockout time from system.