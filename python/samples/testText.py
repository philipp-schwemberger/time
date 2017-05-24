#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)

    def Run(self):
        offscreenCanvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../fonts/10x20.bdf")
        textColor = graphics.Color(255, 255, 255)
        posX = 0
        posY = offscreenCanvas.height/2 + 5
        myText = "8223%"
        num = 98

        while True:
            offscreenCanvas.Clear()
            
            myText = str(num) + "%"

            # draw to see how long the text is and set posX accordingly, then .Clear() to not draw first posX
            length = graphics.DrawText(offscreenCanvas, font, posX, posY, textColor, myText)
            posX = offscreenCanvas.width/2 - length/2
            offscreenCanvas.Clear()

            graphics.DrawText(offscreenCanvas, font, posX, posY, textColor, myText)
            offscreenCanvas = self.matrix.SwapOnVSync(offscreenCanvas)

            time.sleep(1) #position important ? maybe after swapOnSync
            num += 1


# Main function
if __name__ == "__main__":
    parser = RunText()
    if (not parser.process()):
        parser.print_help()
