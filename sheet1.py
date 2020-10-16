# import time
# from OmegaExpansion import oledExp
from dlmode import RUN_MODE
from modeselection import MODES
from oledScreens import OLEDSCREENS


k = MODES()         #mode selection through keypad
disp = OLEDSCREENS()

if __name__ == "__main__":
    disp.WelcomeMessage()
    disp.ModesOfDataLogger()
    userDelay1 = 0
    del disp
    while True:
        k.modeSelection()           #Selection of mode through keypad
        userDelay1 = userDelay1+1
        if userDelay1 == 200:
            RUN_MODE()
