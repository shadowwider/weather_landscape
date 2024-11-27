




import os
from PIL import Image


from p_weather.openweathermap import OpenWeatherMap
from p_weather.sprites import Sprites
from p_weather.draw_weather import DrawWeather

import secrets


class WeatherLandscape:

    TMP_DIR = "tmp"
    OUT_FILENAME = "test_"
    OUT_FILEEXT = ".bmp"
    TEMPLATE_FILENAME = "p_weather/template.bmp"
    SPRITES_DIR="p_weather/sprite"
    DRAWOFFSET = 65


    def __init__(self):
        assert secrets.OWM_KEY != "000000000000000000", "Set OWM_KEY variable to your OpenWeather API key in secrets.py"
        pass




    def MakeImage(self)->Image:
        owm = OpenWeatherMap(secrets.OWM_KEY,secrets.OWM_LAT,secrets.OWM_LON,self.TMP_DIR)
        owm.FromAuto()

        img = Image.open(self.TEMPLATE_FILENAME)

        spr = Sprites(self.SPRITES_DIR,img)

        art = DrawWeather(img,spr)
        art.Draw(self.DRAWOFFSET,owm)

        return img



    def SaveImage(self)->str:
        img = self.MakeImage() 
        placekey = OpenWeatherMap.MakePlaceKey(secrets.OWM_LAT,secrets.OWM_LON)
        outfilepath = self.TmpFilePath(self.OUT_FILENAME+placekey+self.OUT_FILEEXT)
        img.save(outfilepath) 
        return outfilepath

    def SaveImage2(self)->str:
        img = self.MakeImage()
        img = img.rotate(-90, expand=True)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)

        img.save('/var/www/html/test.bmp')
        return '/var/www/html/test.bmp'
        
        
        

    def TmpFilePath(self,filename):
        return os.path.join(self.TMP_DIR,filename)

    '''
    server_name _;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }
        location /chat {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    '''
