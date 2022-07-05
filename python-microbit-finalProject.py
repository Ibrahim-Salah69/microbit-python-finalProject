from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
initialize()
clear_oled()

pulseList = []

while True:
    if pin2.read_digital() == 1:
        #pulseList.clear()
        if pin1.read_digital() == 1:
            pin16.write_analog(1000)
            pulseList.append(1000)
            sleep(100)

        else:=
            pin16.write_analog(0)
            pulseList.append(0)
            sleep(100)

    add_text(0, 0, str(pulseList))

    if pin0.read_digital() == 1:
        for i in pulseList:
            pin16.write_analog(i)
            sleep(100)

