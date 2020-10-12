import copy
import omega_gpio
import time


class KEYPAD:
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

    def getPressKey(self):
        while True:
            self.keypad_init()
            rpos = 0
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
                        self.keycode = self.key[x][y]
                        if self.values[x][y] == 1:
                            return self.keycode

            lastvalues = copy.deepcopy(self.values)


    def checkKey(self):
        a = [0, 1, 2, 3, 11, 18, 8, 9]
        r = [0, 1, 2, 3]
        c = [18, 11, 8, 9]

        key = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"],
        ]

        values = [
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
            ["0", "0", "0", "0"],
        ]

        lastvalues = copy.deepcopy(values)

        # close before open if used
        for pin in a:
            try:
                omega_gpio.closepin(pin)
            except:
                e = 1  # dummy command :-)

        # pin init
        for pin in r:
            omega_gpio.initpin(pin, 'out')

        for pin in c:
            omega_gpio.initpin(pin, 'in')

        if True:
            rpos = 0
            for rpin in r:
                omega_gpio.setoutput(r[0], 0)
                omega_gpio.setoutput(r[1], 0)
                omega_gpio.setoutput(r[2], 0)
                omega_gpio.setoutput(r[3], 0)
                omega_gpio.setoutput(rpin, 1)
                time.sleep(0.05)
                cpos = 0
                for cpin in c:
                    input = omega_gpio.readinput(cpin)
                    values[rpos][cpos] = input
                    cpos = cpos + 1
                rpos = rpos + 1

            for x in range(0, 4):
                for y in range(0, 4):
                    if values[x][y] != lastvalues[x][y]:
                        keycode = key[x][y]
                        if values[x][y] == 1:
                            if keycode == 'D':
                                print("D")
                            elif keycode == 'A':
                                print("A")
                            else:
                                print("Other")
            lastvalues = copy.deepcopy(values)

            ####################################################################################
            ####################################################################################                                                    
if __name__=="__main__":                                                                                                                            
        print("Hello")                                                                                                                              
        k=KEYPAD()                                                                                                                                  
        while True:                                                                                                                                 
                key=k.getPressKey()                                                                                                                 
                print(key)  
