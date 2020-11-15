import os.path
import time

usb_dir_path = '/mnt/sda1'

def runMode():
    print("Run Mode")
    time.sleep(2)

if __name__ == "__main__":
    print("Program start")
    copyDone = 0
    isUSB=0
    while True:
        if isUSB==0:
            copyDone=0
            
        if copyDone==0:
            isUSB = os.path.isdir(usb_dir_path)

        if copyDone==0 and isUSB==1:
            print("EMMC TO USB Copy")
            copyDone=1

        runMode()
        isUSB = os.path.isdir(usb_dir_path)

