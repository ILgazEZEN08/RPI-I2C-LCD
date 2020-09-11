import lcddriver
import time
import datetime

display = lcddriver.lcd()

try:
    print("Writing to display")
    display.lcd_display_string("Zamanin Akiyor", 1) #xD sadece mizah amaçlıdır
    while True:
        display.lcd_display_string(str(datetime.datetime.now().time()), 2)
        
except KeyboardInterrupt:
    print("Cleaning up!")
    display.lcd_clear()
