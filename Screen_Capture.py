from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import pyautogui
import os
from datetime import datetime


def Screen_CAP(FilePath):
    DateTime = datetime.now().strftime("%Y%m%d_%H%M")
    print(DateTime)

    screen = pyautogui.screenshot()


    screen.save(os.path.join(FilePath,DateTime+".jpg"))


##FilePath=r"C:\Users\achan\OneDrive - Ramboll\Desktop\Screen Cap for TimeSheet"

##Screen_CAP(FilePath)
## for testing
##Screen_CAP()