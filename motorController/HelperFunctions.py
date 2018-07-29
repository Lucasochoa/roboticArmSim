from tkinter import *

######################
#HELPER FUNCTIONS
######################




############################################
#Template Helper Functions
############################################
def initSetup(data):
    data.timerDelay = 1
    data.timerTotal = 0
    data.isPaused = True
    data.tree = []
    data.setMode = False
    data.selectedLimb = None
    data.buttons = []
    data.sliders = []

def loadIconImages(data):
    data.loadIconImages = dict()
    refreshFilename = "images/refresh1.gif"
    data.loadIconImages["refresh"] = PhotoImage(file=refreshFilename)

############################################
#DRAWING HELPER FUNCTIONS
############################################

def drawMenu(canvas,data):
    #drawSelectedAnimations(canvas,data)
    canvas.create_rectangle(data.width*(4/5),0,data.width,data.height,
        fill = "grey")
    if data.selectedLimb != None:
        drawMenuHeader(canvas,data.width*(18/20),50,data.selectedLimb.name)

def drawMenuHeader(canvas,x,y,name):
    canvas.create_text(x,y,text="Limb Name: "+name,

                      fill="black", font="Helvetica 16 bold")

def drawSelectedAnimations(canvas,data):
  if data.selectedLimb != None:
    canvas.create_rectangle(0,data.height*(4/5),data.width,data.height,
        fill = "grey")


def drawGrid(canvas,data):
    size = 1
    segment = 20
    width = data.width//segment
    for row in range(width):
        for col in range(width):
            canvas.create_oval(row*segment-size,col*segment-size,
                               row*segment+size,col*segment+size,
                               fill = "grey", outline = '')


def updateSliders(data):
  for slider in data.sliders:
    slider.updateSlider(data)
  for slider in data.EventMenu.sliders:
    slider.updateMenuSliders(data)

#slope formula
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

#distanc formula
def distance(x,y,x2,y2):
        return ((x2-x)**2+(y2-y)**2)**.5
#https://stackoverflow.com/questions/44099594/
#how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners
def round_rectangle(x1, y1, x2, y2,canvas, radius=25, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]

        canvas.create_polygon(points,outline ='black', **kwargs, smooth=True)

#inspired from
#https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
#and
#https://processing.org/reference/map_.html
def map(input,start,stop,start2,stop2):
    pass
    # startRange = start - stop
    # start2Range = start2 - stop2

    # scaledVal = float(input - startRange) / float(start2Range)

    # return start2 + (scaledVal * start2Range)
    #  
def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)