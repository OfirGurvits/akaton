import time
import pyautogui
import threading
from tkinter import *
import queue

def waited():
    # Get the current mouse position
    x, y = pyautogui.position()
    print(f"Position: ({x}, {y})")
    notify_click()


def check_position_after_delay(x,y):
    # Delay for 4 seconds
    time.sleep(4)
    # Check the position after the delay
    position_check()


def runMouse():
    arrayFull=False
    i=0
    myArrray=[]
    while(True):
        if i==40:
            i=0
            arrayFull=True
        time.sleep(0.1)
        if arrayFull:
            boolallEqual=True
            for item in myArrray:
                if item!=arrayFull[0]:
                    boolallEqual=False
                    break

            if boolallEqual:
                waited()

            myArrray.insert(i, pyautogui.position())
            i=(i+1)%40
        else:
            myArrray.insert(i, pyautogui.position())
            i+=1


    # Create the main window
    window = Tk()

    # Create a canvas widget to display the page
    canvas = Canvas(window, width=800, height=600, bg="white")
    canvas.pack()

    # Start the main event loop
    window.mainloop()
