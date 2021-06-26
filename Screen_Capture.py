from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import pyautogui
from datetime import datetime

DateTime = datetime.now().strftime("%Y%m%d-%H%M")
print(DateTime)

screen = pyautogui.screenshot()


screen.save(DateTime+".jpg")

