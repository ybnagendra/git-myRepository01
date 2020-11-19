import datetime
import time
from OmegaExpansion import oledExp
import serial
import RTC_Driver

# Open port with baud rate
ser = serial.Serial(port="/dev/ttyS1", baudrate=115200, timeout=30)


def check_date(year, month, day):
    correctDate = None
    try:
        newDate = datetime.datetime(year, month, day)
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate


class DL_SETTINGS:
    def __init__(self):
        try:
            oledExp.setCursor(3, 0)
            oledExp.write("DataLogger is in Configure mode")
        except:
            pass
        ser.write('\r\n')
        ser.write('Configuration Mode\r\n')
        ser.write("1. Set Date and Time\r\n")
        ser.write("2. To Edit other Parameters \r\n")
        ser.write("3. To Read Configuration\r\n")
        ser.write("Your Selection: ")
        selection = ser.read()
        ser.write(selection)
        time.sleep(2)
        if selection == '':
            print("Run Mode")

        if (selection == '1'):
            print("----------------------SET DATE AND TIME----------------------")
            self.set_date_time()
        elif (selection == '2'):
            print("----------------To Edit Other Parameters---------------")
            self.site_details()
        elif (selection == '3'):
            print("---------------To Read Configuration--------------------")
            self.read_confdata()
        else:
            time.sleep(3)
            ser.write("\r\n")
            self.__init__()

    def set_date_time(self):
        # DS3231 Address
        ds3231 = RTC_Driver.SDL_DS3231(0, 0x68)
        # comment out the next line after the clock has been initialized
        # ds3231.write_now()  # through Wifi
        # ds3231.set_datetime()     #through user input
        ds3231.set_datetime_through_serial()

    def site_details(self):
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
        self.__init__()

    def read_confdata(self):
        f = open('confdata.txt', 'r')
        lines = f.readlines()
        SiteID = lines[0].rstrip('\n')
        MonitoringID = lines[1].rstrip('\n')
        AnalyzerID = lines[2].rstrip('\n')
        ParameterID = lines[3].rstrip('\n')
        ser.write(SiteID)
        ser.write('\r\n')
        ser.write(MonitoringID)
        ser.write('\r\n')
        ser.write(AnalyzerID)
        ser.write('\r\n')
        ser.write(ParameterID)
        ser.write('\r\n')
        time.sleep(5)
        self.__init__()
