from OmegaExpansion import oledExp
import time

class OLEDSCREENS:
    def WelcomeMessage(self):
        oledExp.setVerbosity(0)
        oledExp.driverInit()
        oledExp.clear()
        oledExp.setCursor(3, 0)
        oledExp.write("Welcome to OnionOmega")
        oledExp.setCursor(4, 0)
        oledExp.write("Data Logger Project")
        time.sleep(3)
        oledExp.clear()

    def ModesOfDataLogger(self):
        # oledExp.clear()
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

    def WrongSelectionOfKey(self):
        oledExp.clear()
        oledExp.setCursor(3, 0)
        oledExp.write("Invalid Selection")
        oledExp.setCursor(4, 0)
        oledExp.write("Select 1 or 2 or 3")
        time.sleep(2)
        oledExp.clear()
        self.ModesOfDataLogger()

    def MenuOfConfigureMode(self):
        oledExp.setCursor(7, 0)
        oledExp.write("CONFIGURATION MODE")
        oledExp.setCursor(6, 0)
        oledExp.write("*********************")
        oledExp.setCursor(1, 0)
        oledExp.write("1. SET DATE AND TIME ")
        oledExp.setCursor(2, 0)
        oledExp.write("2. To Edit Other Parameters")
        oledExp.setCursor(3, 0)
        oledExp.write("3. To Read Configuration")
        oledExp.setCursor(4, 0)
        oledExp.write("Your Selection: ")

    def ConfigureMode_Page2(self):
        oledExp.clear()
        oledExp.setCursor(3, 0)
        oledExp.write("Invalid Selection")
        oledExp.setCursor(4, 0)
        oledExp.write("Select 1 or 2 or 3")
        time.sleep(2)
        oledExp.clear()
        self.MenuOfConfigureMode()

    def ConfigureMode_Page3(self):
        oledExp.setCursor(6, 0)
        oledExp.write("CONFIGURATION MODE")
        oledExp.setCursor(7, 0)
        oledExp.write("*********************")
        oledExp.setCursor(3, 0)
        oledExp.write("Connect to PC/Laptop ")
        oledExp.setCursor(4, 0)
        oledExp.write("through USB Cable ")

    def configureMode_Page4(self):
        oledExp.clear()
        oledExp.setCursor(0, 0)
        oledExp.write("CONFIGURATION MODE")
        oledExp.setCursor(1, 0)
        oledExp.write("*********************")
        oledExp.setCursor(2, 0)
        oledExp.write("Configuartion done")
        oledExp.setCursor(7, 0)
        oledExp.write("Press 'B' to go back")









