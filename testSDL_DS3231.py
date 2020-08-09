#!/usr/bin/env python                                                                                                              
#                                                                                                                                  
# Test SDL_DS3231                                                                                                                  
# John C. Shovic, SwitchDoc Labs                                                                                                   
# 08/03/2014                                                                                                                       
#                                                                                                                                  
#                                                                                                                                  
                                                                                                                                   
import time                                                                                                                        
import datetime,pytz                                                                                                               
import SDL_DS3231                                                                                                                  
                                                                                                                                   
# Main Program                                                                                                                     
                                                                                                                                   
print("")                                                                                                                          
print("Test SDL_DS3231 Version 1.0 - SwitchDoc Labs")                                                                              
print("")                                                                                                                          
print("")                                                                                                                          
print("Program Started at:" + time.strftime("%Y-%m-%d %H:%M:%S"))                                                                  
print("")                                                                                                                          
                                                                                                                                   
filename = time.strftime("%Y-%m-%d%H:%M:%SRTCTest") + ".txt"                                                                       
start_time = datetime.datetime.utcnow()                                                                                            
                                                                                                                                   
ds3231 = SDL_DS3231.SDL_DS3231(0, 0x68)                                                                                            
                                                                                                                                   
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
                                                                                                                                   
                               
