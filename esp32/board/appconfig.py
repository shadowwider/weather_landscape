
class AppConfig:
    
    TITLE = "WebFrame"
    
    VERSION = "1.0 OCT 2024" 
    
    PIN_CLK = 18
    PIN_DIN = 23 # MOSI
    PIN_DOUT = 19 # MISO, not used
    PIN_CS = 5
    PIN_DC = 13
    PIN_RST = 12
    PIN_BUSY = 14
    
    PIN_LED = 2
    
    
    IMAGE_RELOAD_PERIOD_MS = 15*60*1000


    SCR_WIDTH = 128
    SCR_HEIGHT = 296
    SCR_BYTES_PER_LINE = int(SCR_WIDTH/8)
    

    AP_SSID = ''
    AP_PASS = ''
  
    
    URL = "<url that points to the bmp image>"
    
    ERROR_RETRY_SEC = 30*60
    
    
    
    def print(self):
        print("***",self.TITLE,"***    Ver. ",self.VERSION)
        print("EInk ",self.SCR_WIDTH,"x",self.SCR_HEIGHT)
        print("Pin CLK =", self.PIN_CLK)
        print("Pin DIN =", self.PIN_DIN) 
        print("Pin CS =", self.PIN_CS)
        print("Pin DC =", self.PIN_DC)
        print("Pin RST =", self.PIN_RST)
        print("Pin BUSY =", self.PIN_BUSY)
        print("Pin LED =", self.PIN_LED)
        print("SSID", self.AP_SSID)
        print("PASS", self.AP_PASS)
        print("URL", self.URL)
        
        
        
    

    