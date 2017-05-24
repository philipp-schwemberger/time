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

gpsd = None #seting the global variable

class GpsPoller(threading.Thread):

  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true

  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer


class TimeInPercent(SampleBase):
    def __init__(self, *args, **kwargs):
        super(TimeInPercent, self).__init__(*args, **kwargs)

    def Run(self):
        #create Canvas and set up graphics
        offscreenCanvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../fonts/percent16.bdf")
        font2 = graphics.Font()
        font2.LoadFont("../../fonts/4x6.bdf")
        textColor = graphics.Color(255, 255, 255)
        posX = 0
        posY = offscreenCanvas.height/2 + 5 #font height/2
        myText = ""

        global gpsp # I had to add this because it complained about var
        gpsp = GpsPoller() # create the thread
        try:
            gpsp.start() # start it up

            while True:
                t = time.time()
                st = datetime.datetime.fromtimestamp(t).strftime('%S')
                #print(st)
                print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
                hours = gpsd.utc[11:13]
                minutes = gpsd.utc[14:16]
                seconds = gpsd.utc[17:19]
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


                    offscreenCanvas.Clear()
                    myText = str(percent) + "%"
                    sysTime = hours + ":" + minutes + ":" + seconds 

                    # draw to see how long the text is and set posX accordingly, then .Clear() to not draw first posX
                    length = graphics.DrawText(offscreenCanvas, font, posX, posY, textColor, myText)
                    posX = offscreenCanvas.width/2 - length/2
                    offscreenCanvas.Clear()

                    graphics.DrawText(offscreenCanvas, font, posX, posY, textColor, myText)

                    #show real system time
                    #graphics.DrawText(offscreenCanvas, font2, 10, offscreenCanvas.height-3, textColor, sysTime)
                    offscreenCanvas = self.matrix.SwapOnVSync(offscreenCanvas)
                


                time.sleep(2) #set to whatever

        except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
            print "\nKilling Thread..."
            gpsp.running = False
            gpsp.join() # wait for the thread to finish what it's doing
        print "Done.\nExiting."


# Main function
if __name__ == "__main__":
    parser = TimeInPercent()
    if (not parser.process()):
        parser.print_help()
        






