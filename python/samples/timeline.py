#!/usr/bin/env python
from samplebase import SampleBase
import time
import datetime

class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def Run(self):
        offsetCanvas = self.matrix.CreateFrameCanvas()     

        while True:
            t = time.time()
            st = datetime.datetime.fromtimestamp(t).strftime('%S')
            print(st)
            st = int(st)

            length = st #offsetCanvas.width/2
            if length == 0:
                for x in range(0, offsetCanvas.width):
                    offsetCanvas.SetPixel(x, offsetCanvas.height/2, 0, 255, 0)   
            for x in range(0, length):
                offsetCanvas.SetPixel(x, offsetCanvas.height/2, 255, 0, 0)  

            offsetCanvas = self.matrix.SwapOnVSync(offsetCanvas)


# Main function
if __name__ == "__main__":
    parser = SimpleSquare()
    if (not parser.process()):
        parser.print_help()
