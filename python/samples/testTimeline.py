#!/usr/bin/env python
from samplebase import SampleBase
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


class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def Run(self):
        offsetCanvas = self.matrix.CreateFrameCanvas()

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
                    totalMinutes = int(hours)*60 + int(minutes)
                    print('total minutes of day: ' + str(totalMinutes))

                    percent = (totalMinutes/float(1440))
                    msg = 'percent of the day: ' + str(percent)
                    #msg = 'percent of the day: ' + str(percent)
                    print(msg)

                st = int(st)        
                length = st #offsetCanvas.width/2      
                if length == 0:
                    for x in range(0, offsetCanvas.width):
                        offsetCanvas.SetPixel(x, offsetCanvas.height/2, 0, 255, 0)   
                for x in range(0, length):
                    offsetCanvas.SetPixel(x, offsetCanvas.height/2, 255, 0, 0)  

                offsetCanvas = self.matrix.SwapOnVSync(offsetCanvas)

                time.sleep(1) #set to whatever

        except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
            print "\nKilling Thread..."
            gpsp.running = False
            gpsp.join() # wait for the thread to finish what it's doing
        print "Done.\nExiting."


# Main function
if __name__ == "__main__":
    parser = SimpleSquare()
    if (not parser.process()):
        parser.print_help()
        






