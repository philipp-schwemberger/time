#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import datetime

import os
from gps import *
from time import *
import time
import threading


class TimeInPercent(SampleBase):
    def __init__(self, *args, **kwargs):
        super(TimeInPercent, self).__init__(*args, **kwargs)

    def Run(self):
        #create Canvas and set up graphics
        screenCanvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../fonts/10x20.bdf")
        #font.LoadFont("../../PourcentFont3-2.ttf")
        font2 = graphics.Font()
        font2.LoadFont("../../fonts/4x6.bdf")
        textColor = graphics.Color(255, 0, 0)
        posX = 0
        posY = screenCanvas.height/2 + 5 #font height/2
        myText = ""



        while True:
            t = datetime.datetime.now()
           
            hours = t.strftime('%H')
            minutes = t.strftime('%M')
            seconds = t.strftime('%S')

            print('hour: ' + hours)
            print('minute: ' + minutes)
            print('second: ' + seconds)
            
            if hours != '':
                # +2 time correction
                totalMinutes = (int(hours)+2)*60 + int(minutes)
                print('total minutes of day: ' + str(totalMinutes))

                percent = int(totalMinutes/float(1440)*100)
                msg = 'percent of the day: ' + str(percent)
                #msg = 'percent of the day: ' + str(percent)
                print(msg)


                screenCanvas.Clear()
                myText = str(percent) + "%"
                sysTime = hours + ":" + minutes + ":" + seconds 

                # draw to see how long the text is and set posX accordingly, then .Clear() to not draw first posX
                length = graphics.DrawText(screenCanvas, font, posX, posY, textColor, myText)
                posX = screenCanvas.width/2 - length/2
                screenCanvas.Clear()

                graphics.DrawText(screenCanvas, font, posX, posY, textColor, myText)
                
                #show real system time
                graphics.DrawText(screenCanvas, font2, 10, screenCanvas.height-3, textColor, sysTime)

                if int(seconds)%2 == 0:
                    print("true")
                    screenCanvas.SetPixel(0, screenCanvas.height-1, 255, 0, 0)
                else:
                    screenCanvas.SetPixel(0, screenCanvas.height-1, 0, 0, 0)
                    print("false")
                screenCanvas = self.matrix.SwapOnVSync(screenCanvas)
            
                


            time.sleep(0.5) #set to whatever



# Main function
if __name__ == "__main__":
    parser = TimeInPercent()
    if (not parser.process()):
        parser.print_help()
        






