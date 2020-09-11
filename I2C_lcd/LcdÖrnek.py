import lcddriver
import time
display = lcddriver.lcd()
try:
    while True:
        print("Lcd calisiyor")
        display.lcd_display_string("S.A.dunya ", 1) 
        display.lcd_display_string("LCD I2C ", 2) 
        time.sleep(2)
        display.lcd_clear()
        time.sleep(1)
        display.lcd_display_string("HEllo xD", 1) 
        time.sleep(2)                                    
        display.lcd_clear()                               
        time.sleep(2)                                     
except KeyboardInterrupt: 
    print("Temizleniyor")
    display.lcd_clear()
