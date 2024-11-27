from appconfig import AppConfig
from wifi import WiFi

from led import Led,LedDummy

from epd import EPD_2in9_Landscape,EPD_2in9_Portrait
import time
from machine import deepsleep




def print_error(text):
    global error_count 
    print_message("Error: %s (%i)" % (text,error_count))
    error_count+=1
    time.sleep(cfg.ERROR_RETRY_SEC)
    


cfg = AppConfig()
#led = Led(cfg.PIN_LED)
led = LedDummy()
wlan = WiFi(cfg,led)

eink = EPD_2in9_Portrait()
cfg.print()
print("------")

#print_message(GetResetCauseText())
#time.sleep(10)





error_count = 0


while (True):
    
    rc = wlan.connect()
    if (not rc):
        #print("WiFi connection failed.")
        continue
    
    img = wlan.load()

    if (img):
        eink.display(img)
        eink.sleep()  # Call the sleep method after displaying the image
    else:
        print("Image load failed.")
        continue
    
    #
    deepsleep(cfg.IMAGE_RELOAD_PERIOD_MS)




    
    
    

