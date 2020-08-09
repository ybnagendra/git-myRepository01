from datetime import datetime                                                                                                      
from OmegaExpansion import onionI2C                                                                                                
                                                                                                                                   
import time                                                                                                                  
                                                                                                                  
                                                                                                                                                                                                                                         
class SDL_DS3231():                                                                                                                
    _REG_SECONDS = 0x00                                                                                                            
    _REG_MINUTES = 0x01                                                                                                            
    _REG_HOURS = 0x02                                                                                                              
    _REG_DAY = 0x03                                                                                                                
    _REG_DATE = 0x04                                                                                                               
    _REG_MONTH = 0x05                                                                                                              
    _REG_YEAR = 0x06                                                                                                               
    _REG_CONTROL = 0x07                                                                                                            
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
    ###########################                                                                                                    
    # DS3231 Code                                                                                                                  
    ###########################                                                                                                    
    def __init__(self, twi=0, addr=0x68, at24c32_addr=0x56):                                                                       
        # self._bus = smbus.SMBus(twi)                                                                                             
        self._i2c = onionI2C.OnionI2C(twi)                                                                                         
        self._addr = addr                                                                                                          
        self._at24c32_addr = at24c32_addr                                                                                                                                                                                                                                                                                           
                                                                                                                                   
    ###########################                                                                                                    
    # AT24C32 Code                                                                                                                 
    ###########################                                                                                                    
                                                                                                                                   
    # def set_current_AT24C32_address(self,address):                                                                               
    #  a0=address%256;                                                                                                             
    #  a1=address/256;                                                                                                             
    #  self._bus.write_i2c_block_data(self._at24c32_addr,a1,[a0])                                                                  
                                                                                                                                   
                                                                                                                                   
    def read_AT24C32_byte(self, address):                                                                                          
        #print "i2c_address =0x%x eepromaddress = 0x%x  " % (self._at24c32_addr, address)                                          
                                                                                                                                   
        # self.set_current_AT24C32_address(address)                                                                                
        # return self._bus.read_byte(self._at24c32_addr)                                                                           
        return self._i2c.readBytes(self._at24c32_addr, address, 1)                                                                 
                                                                                                                                   
                                                                                                                                   
    def write_AT24C32_byte(self, address, value):                                                                                  
        #print "i2c_address =0x%x eepromaddress = 0x%x value = 0x%x %i " % (self._at24c32_addr, address, value, value)             
        # a1=address/256;                                                                                                          
        # a0=address%256;                                                                                                          
        # self._bus.write_i2c_block_data(self._at24c32_addr,a1,[a0, value])                                                        
        self._i2c.writeBytes(self._at24c32_addr,address,value)                                                                     
        time.sleep(0.20)                                     
