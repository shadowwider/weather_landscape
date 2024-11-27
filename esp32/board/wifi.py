import network
import urequests
import time

def lebytes_to_int(bytes):
    return int.from_bytes(bytes, 'little')


class WiFi:
    
    
    def __init__(self,appcfg,led):
        self.led = led
        self.cfg = appcfg
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        print("WiFi init")
        
        
    def connect(self):
        if self.wlan.isconnected():
            print("WiFi already connected: ", self.wlan.ifconfig())
            self.led.blink(1)
            return True
            
        self.led.blink()
        print('Trying to connect to %s...' % self.cfg.AP_SSID)
        if not self.wlan.active():
            print("Failed to activate WLAN interface.")
            self.wlan.active(True)
        try:
            self.wlan.connect(self.cfg.AP_SSID, self.cfg.AP_PASS )
        except OSError as e:
            print(f"WiFi connection error----: {e}")
        for retry in range(200):
            connected = self.wlan.isconnected()
            if connected:
                break
            time.sleep(0.1)
            print('.', end='')
        if connected:
            print('\nConnected. Network config: ', self.wlan.ifconfig())
            self.led.off()
        else:
            print('\nFailed.')
            self.led.flash()
            
        return connected
    
    
    def load(self):
        print("Loading "+self.cfg.URL)
        
        self.led.blink()
        r = urequests.get(self.cfg.URL, headers={'accept': 'image/bmp'})
    
        if (r==None) or (r.content==None) or (len(r.content)<54):
            return None
    
        img_bytes = r.content
        start_pos = lebytes_to_int(img_bytes[10:14])
        end_pos = start_pos + lebytes_to_int(img_bytes[34:38])
        width = lebytes_to_int(img_bytes[18:22])
        height = lebytes_to_int(img_bytes[22:26])
        
        if (width!=self.cfg.SCR_WIDTH) or (height!=self.cfg.SCR_HEIGHT):
            print("Wrong image size",width,height)
        
        print("Image loaded")
        
        self.led.off()

        return img_bytes[start_pos:]
            
            

        
    
