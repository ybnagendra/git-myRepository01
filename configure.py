import time
import serial
import RTC_Driver
from OmegaExpansion import oledExp
import datetime
from oledScreens import OLEDSCREENS
from modeselection import MODES

k = MODES()         #mode selection through keypad
disp = OLEDSCREENS()


# Open port with baud rate
ser = serial.Serial(port="/dev/ttyS1", baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    timeout=100)


def check_date(year, month, day):
    correctDate = None
    try:
        newDate = datetime.datetime(year, month, day)
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate


class DL_SETTINGS:
    def set_date_time(self):
        # DS3231 Address
        ds3231 = RTC_Driver.SDL_DS3231(0, 0x68)
        # comment out the next line after the clock has been initialized
        # ds3231.write_now()  # through Wifi
        # ds3231.set_datetime()     #through user input
        ds3231.set_datetime_through_keypad()


    def site_details(self):
        disp.ConfigureMode_Page2()
        siteId = ''
        monitoringId = ''
        analyzerId = ''
        parameterId = ''
        while len(siteId) == 0:
            # Serial input
            ser.write('Enter site ID: ')
            siteId = ser.read()  # read serial port
            time.sleep(0.03)
            data_left = ser.inWaiting()  # check for remaining byte
            siteId += ser.read(data_left)
            ser.write(siteId + '\r\n')
            oledExp.clear()
            oledExp.setCursor(1, 0)
            oledExp.write(siteId)
            time.sleep(1)
        while len(monitoringId) == 0:
            ser.write('Enter monitoring ID: ')
            monitoringId = ser.read()  # read serial port
            time.sleep(0.03)
            data_left = ser.inWaiting()  # check for remaining byte
            monitoringId += ser.read(data_left)
            ser.write(monitoringId + '\r\n')
            oledExp.setCursor(2, 0)
            oledExp.write(monitoringId)
            time.sleep(1)
        while len(analyzerId) == 0:
            ser.write('Enter analyserID: ')
            analyzerId = ser.read()  # read serial port
            time.sleep(0.03)
            data_left = ser.inWaiting()  # check for remaining byte
            analyzerId += ser.read(data_left)
            ser.write(analyzerId + '\r\n')
            oledExp.setCursor(3, 0)
            oledExp.write(analyzerId)
            time.sleep(1)
        while len(parameterId) == 0:
            ser.write('Enter ParameterID: ')
            parameterId = ser.read()  # read serial port
            time.sleep(0.03)
            data_left = ser.inWaiting()  # check for remaining byte
            parameterId += ser.read(data_left)
            ser.write(parameterId + '\r\n')
            oledExp.setCursor(4, 0)
            oledExp.write(parameterId)

        f = open('confdata.txt', 'w')
        f.write(siteId + '\n')
        f.write(monitoringId + '\n')
        f.write(analyzerId + '\n')
        f.write(parameterId + '\n')
        time.sleep(5)
        disp.configureMode_Page4()
        userDelay3 = 0
        while True:
            k.listOfConfigureMode()
            userDelay3 = userDelay3 + 1
            if userDelay3 == 60:
                print("RUN MODE")
                while True:
                    pass

    def read_confdata(self):
        f = open('confdata.txt', 'r')
        lines = f.readlines()
        SiteID = lines[0].rstrip('\n')
        MonitoringID = lines[1].rstrip('\n')
        AnalyzerID = lines[2].rstrip('\n')
        ParameterID = lines[3].rstrip('\n')
        oledExp.clear()
        oledExp.setCursor(0, 0)
        oledExp.write(SiteID)
        oledExp.setCursor(1, 0)
        oledExp.write(MonitoringID)
        oledExp.setCursor(2, 0)
        oledExp.write(AnalyzerID)
        oledExp.setCursor(3, 0)
        oledExp.write(ParameterID)
        #self.goto_menu()

    def goto_menu(self):
        oledExp.setCursor(5,0)
        oledExp.write("Press '#' to return")
        oledExp.setCursor(6, 0)
        oledExp.write("Main Menu")
        key2=k.getPressKey()
        if key2=='#':
            oledExp.setCursor(7, 0)
            oledExp.write(key2)
            time.sleep(2)
            oledExp.clear()
            self.__init__()


