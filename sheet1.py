import time
from OmegaExpansion import oledExp
from dlmode import RUN_MODE
from aaa1 import DL_MODES


def welcomeMessage():
    oledExp.setVerbosity(0)
    oledExp.driverInit()
    oledExp.clear()
    oledExp.setCursor(3, 0)
    oledExp.write("Welcome to OnionOmega")
    oledExp.setCursor(4, 0)
    oledExp.write("Data Logger Project")
    time.sleep(5)


def displayModes():
    oledExp.clear()
    oledExp.setCursor(2, 0)
    oledExp.write("Select mode(1,2,3):")
    oledExp.setCursor(3, 0)
    oledExp.write("1. CONFIGURE MODE")
    oledExp.setCursor(4, 0)
    oledExp.write("2. RUN MODE")
    oledExp.setCursor(5, 0)
    oledExp.write("3. BACKUP MODE")
    oledExp.setCursor(6, 0)
    oledExp.write("Mode of Operation:")


if __name__ == "__main__":
    welcomeMessage()
    timeCount1=0
    while True:
        displayModes()
        # Wait for user keypad input
        DL_MODES.modeSelection()
        oledExp.clear()
        timeCount1=timeCount1+1
        time.sleep(1)
        if timeCount1==60:
            RUN_MODE()
