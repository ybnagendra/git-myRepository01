import copy
import omega_gpio
import time
import dlmode
import configure
from OmegaExpansion import oledExp

class DL_MODES:
    def keypad_init(self):
        self.a = [0, 1, 2, 3, 11, 18, 8, 9]
        self.r = [0, 1, 2, 3]
        self.c = [18, 11, 8, 9]

        self.key = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"],
        ]

        self.values = [
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
        ]

        self.lastvalues = copy.deepcopy(self.values)

        # close before open if used
        for pin in self.a:
            try:
                omega_gpio.closepin(pin)
            except:
                e = 1  # dummy command :-)

        # pin init
        for pin in self.r:
            omega_gpio.initpin(pin, 'out')

        for pin in self.c:
            omega_gpio.initpin(pin, 'in')
            
            
    def modeSelection(self):
        self.keypad_init()
        rpos=0
        if True:
            for rpin in self.r:
                omega_gpio.setoutput(self.r[0], 0)
                omega_gpio.setoutput(self.r[1], 0)
                omega_gpio.setoutput(self.r[2], 0)
                omega_gpio.setoutput(self.r[3], 0)
                omega_gpio.setoutput(rpin, 1)
                time.sleep(0.05)
                cpos = 0
                for cpin in self.c:
                    input = omega_gpio.readinput(cpin)
                    self.values[rpos][cpos] = input
                    cpos = cpos + 1
                rpos = rpos + 1

            for x in range(0, 4):
                for y in range(0, 4):
                    if self.values[x][y] != self.lastvalues[x][y]:
                        keycode = self.key[x][y]
                        if self.values[x][y] == 1:
                            if keycode == '1':
                                oledExp.setCursor(7, 0)
                                oledExp.write(keycode)
                                configure.DL_SETTINGS()
                                dlmode.RUN_MODE()
                            elif keycode == '2':
                                oledExp.setCursor(7, 0)
                                oledExp.write(keycode)
                                dlmode.DIRECT_RUN_MODE()
                            elif keycode == '3':
                                oledExp.setCursor(7, 0)
                                oledExp.write(keycode)
                                dlmode.DIRECT_BACKUP_MODE()
                            else:
                                oledExp.write("Invalid Selection")
                                oledExp.write("Select 1 or 2 or 3")
                                time.sleep(2)
            lastvalues = copy.deepcopy(self.values)
   
