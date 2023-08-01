from RPLCD.i2c import CharLCD
from datetime import datetime
import time

# Replace 0x27 with the I2C address of your LCD module
lcd = CharLCD('PCF8574', 0x27)

try:
    while True:
        # Get the current time and date
        current_time = datetime.now().strftime("%I:%M:%S %p")
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Display the time and date on the LCD
        lcd.clear()
        lcd.write_string(f"Time: {current_time}")
        lcd.crlf()  # Move to the second line
        lcd.write_string(f"Date: {current_date}")

        time.sleep(1)  # Wait for 1 second before updating the display

except KeyboardInterrupt:
    lcd.clear()  # Clear the LCD before exiting
    lcd.write_string("Exiting...")
    time.sleep(2)  # Wait for 2 seconds before fading out

    # Fade out the LCD by gradually reducing the brightness
    for brightness in range(100, 0, -10):
        lcd.backlight_enabled = False
        time.sleep(0.1)
        lcd.backlight_enabled = True
        lcd.brightness = brightness

    lcd.clear()  # Clear the screen

