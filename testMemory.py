import time                                                                                                                        
import datetime,pytz                                                                                                               
import EEPROM                                                                                                                 
                                                                                                                                   
                                                                                                                                                                                                                                                                                                                   
start_time = datetime.datetime.utcnow()                                                                                            
                                                                                                                                   
ds3231 = EEPROM.SDL_DS3231(0, 0x68)                                                                                            
                                                                                                                                   
# comment out the next line after the clock has been initialized                                                                   
# ds3231.write_now()                                                                                                               
                                                                                                                                   
# Main Loop - sleeps 10 seconds, then reads and prints values of all clocks                                                        
                                                                                                                                   
while True:                                                                                                                        
    now_utc = datetime.datetime.utcnow()                                                                                           
    local_tz = pytz.timezone('Asia/Kolkata')                                                                                       
    now_utc = pytz.utc.localize(now_utc)                                                                                           
    x = now_utc.astimezone(local_tz)                                                                                               
                                                                                                                                   
    current_time = x                                                                                                               
    #deltaTime = current_time - start_time                                                                                         
    print(current_time)                                                                                                            
    print("Raspberry Pi=\t" + time.strftime("%Y-%m-%d %H:%M:%S"))                                                                  
    print("DS3231=\t\t%s" % ds3231.read_datetime())                                                                                
    time.sleep(5)                                                                                                                  
    print("")                                                                                                                      
                                  
