{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from datetime import datetime\
import time\
\
try:\
    while True:\
        # Get the current time and date\
        current_time = datetime.now().strftime("%I:%M:%S %p")\
        current_date = datetime.now().strftime("%Y-%m-%d")\
\
        # Display the time and date in the terminal\
        print(f"Time: \{current_time\}")\
        print(f"Date: \{current_date\}")\
\
        time.sleep(1)  # Wait for 1 second before updating the display\
\
except KeyboardInterrupt:\
    print("Exiting...")\
    time.sleep(2)  # Wait for 2 seconds before clearing the screen\
}