#!/usr/bin/env python
from samplebase import SampleBase

class SimpleSquare(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleSquare, self).__init__(*args, **kwargs)

    def Run(self):
        offsetCanvas = self.matrix.CreateFrameCanvas()
        while True:
        
		length = offsetCanvas.width/2	
  
		for x in range(0, length):
			offsetCanvas.SetPixel(x, offsetCanvas.height/2, 255, 0, 0)  
	
		offsetCanvas = self.matrix.SwapOnVSync(offsetCanvas)


# Main function
if __name__ == "__main__":
    parser = SimpleSquare()
    if (not parser.process()):
        parser.print_help()
