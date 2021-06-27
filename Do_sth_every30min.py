from time import sleep
from datetime import datetime
from Screen_Capture import Screen_CAP


def run(condition):
    while datetime.now().minute not in {30}:  # Wait 1 second until we are synced up with the 'every 30 minutes' clock
        sleep(1)

    while condition == True:
        sleep(30*60)  # Wait for 30 minutes
        Screen_CAP()

##Test
###run(True)