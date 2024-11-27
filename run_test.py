import os


from weather_landscape import WeatherLandscape





w = WeatherLandscape()

fn = w.SaveImage()

print("Saved",fn)

'''
import os

from datetime import datetime
from weather_landscape import WeatherLandscape





w = WeatherLandscape()

fn = w.SaveImage2()

print("Saved",fn)
with open("/root/weather_landscape/task_log.txt", "a") as log:
    log.write("Task executed successfully at {}\n".format(datetime.now()))
'''
    
