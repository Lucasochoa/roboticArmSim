from tkinter import *

from HelperFunctions import *

from EventMenu import *
from RotationEvent import *
from StopEvent import *
from PlayButton import *
from ToggleButton import *
from RadialDial import *
from Slider import *
from Joint import *
from Button import *
from LimbButton import *
#import tkinter as tk

import math

####################################
#Helper Functions
####################################
#recursively updates through limbs to reduce delay
def recursiveUpdate(data):
    limb = data.tree[0]
    if limb.children == None:
        pass
    else:
        for limbs in limb.children.recursiveUpdate()

def completeRecursiveUpdate(limb):
    if limb.children == None:
        if self.parent != None:
            self.x = self.parent.x2
            self.y = self.parent.y2
    else:
        for tempLimb in limb.children:
            tempLimb.completeRecursiveUpdate(tempLimb)

    #check if has child, if has child call update
    #else call again on set of children
    
#refreshes xy position
def updateAll(data):
    if len(data.tree) > 0:
        for limb in data.tree:
            limb.update()

#draws all limbs and updates them (fix at some point breaks MVC)
def drawAllLimbs(canvas,data):
    if len(data.tree) > 0:
        if data.selectedLimb != None:
            data.selectedLimb.drawRotationDial(canvas,data)

            #data.selectedLimb.drawLimmitDial(canvas,data)

        for limb in data.tree:
            updateAll(data) #updating everything too much    
            #limb.updateChildren()
            limb.draw(canvas)

####################################
#Animation Template
#from 15112 course website
####################################

def init(data):
    initSetup(data)
    loadIconImages(data)

    data.tempTime = 0
    
    rotationSlider = Slider("rotation",data.width*(17/20),150,150,25,0,100)
    speedSlider = Slider("speed",data.width*(17/20),200,150,25,0,100)
    lengthSlider = Slider("length",data.width*(17/20),250,150,25,0,100)
    data.sliders.extend([rotationSlider,speedSlider,lengthSlider])

    #data.radialDialTest = RadialDial(500,500,200,0,0)
    data.EventMenu = EventMenu("event menu",data.width*(4/5),data.height/2,data)

    data.playButton = PlayButton("play",50,50,100,50)
    data.testLimbButton = LimbButton("test",50,120,100,100)
    data.switchButton =  ToggleButton("switch direction",
        data.width*(17/20),300,140,50)

    #data.button.extend([limbButton,playButton])
    
#returns selected limb
def clickLimbs(event,data):
    for limb in data.tree:
        selectedLimb = limb.clicked(event,data)
        #print(selectedLimb)
        if selectedLimb != None:
            return selectedLimb
    return None


 #combine this with clickLimbs
def checkForAttachment(event,data):
    if data.tree != []:
        for limb in data.tree:
             tempLimb = limb.endNodeClicked(event,data)
             if tempLimb != None:
                return tempLimb
    return None

def addEvent(limb):
    newEvent = RotationEvent("clockwise",1,30)
    newEvent2 = RotationEvent("counterClockwise",-1,20)
    stopEvent = StopEvent("stop",10)
    limb.addEvent(newEvent)
    limb.addEvent(newEvent2)
    limb.addEvent(stopEvent)

def mousePressed(event,data):
    #logic for limb identification
    #checkForAttachment(event,data)
    selectedLimb = clickLimbs(event,data)
    #slider logic
    
    #logic for play button
    if data.playButton.clicked(event,data):
        data.isPaused = not data.isPaused

    sliderEvent = False
    for slider in data.sliders:
        if slider.mouseClickedDown(event):
            sliderEvent = True

    if data.switchButton.clicked(event,data):
        if data.selectedLimb != None:
            data.selectedLimb.direction *= -1

    elif data.EventMenu.clicked(event,data):
        pass

    elif sliderEvent != False:
        pass

    elif data.setMode == False and data.testLimbButton.clicked(event,data):
        data.setMode = True
        newJoint = Joint('test',event.x,event.y,data)
        #joint add event
        addEvent(newJoint)
        data.tree.append(newJoint)
        data.selectedLimb = newJoint

    #for picking up new limb
    elif data.setMode == False and selectedLimb != None:
        data.setMode = True
        data.selectedLimb = selectedLimb

    #dropping limb
    else:
        data.selectedLimb = None
        pass
    updateSliders(data)
        

def mouseMoved(event,data):
    #data.radialDialTest.mouseMoved(event,data)
    data.EventMenu.mouseMoved(event,data)

    for slider in data.sliders:
        slider.mouseMoved(event,data)

    data.isPaused = True
    if data.setMode:
        x, y = event.x, event.y
        if data.selectedLimb != None:
            data.selectedLimb.x = x
            data.selectedLimb.y = y

def mouseReleased(event,data,canvas):
    #slider controls
    for slider in data.sliders:
        slider.mouseReleased(event)

    data.setMode = False
    # check for overlap and define relationships
    checkedLimb = checkForAttachment(event,data)
    #print(checkedLimb)
    if checkedLimb != None:
        print("working")
        checkedLimb.setChild(data.selectedLimb)
        clickedLimb = None
    data.EventMenu.mouseReleased(event)
    data.testLimbButton.mouseRemoved(event,data)


def keyPressed(event, data):
    if event.keysym == 'p':
        data.isPaused = not data.isPaused
    elif event.keysym == 'Left':
        data.selectedLimb.rotate(-45)
    elif event.keysym == 'Right':
        data.selectedLimb.rotate(45)
    elif event.keysym == 't':
        for event in data.selectedLimb.events:
            print(event.name,"duration",event.duration,"start",event.startTime)
    elif event.keysym == 'r':
        data.selectedLimb.updateEvents()


def rotateForDuration(limb,direction,amount,data):
    data.tempTime += 1

    if data.tempTime < amount:
        print("first")
        limb.rotate(data.selectedLimb.speed*direction)


    elif data.tempTime >= amount and data.tempTime< amount + 3:
        print("second")
        limb.rotate(data.selectedLimb.speed*direction*-1)

    else:
        print("third")
        data.tempTime = 0

# def testProofOfConcept(limb,direction,amount,data)
#     data.tempTime += 1
#     if data.tempTime < amount:
#     else



def timerFired(data):
    if not data.isPaused:
        data.timerTotal +=1
        #print(data.timerTotal)
        if data.timerTotal % 1 == 0:
            updateSliders(data)
            #rotateForDuration(data.selectedLimb,1,2,data)

            #rotateForDuration(data.selectedLimb,-1,2)

            #data.selectedLimb.rotate(data.selectedLimb.speed*\
            #    data.selectedLimb.direction)

            for i in range(len(data.tree)):
                limb = data.tree[i]
                limb.playEvents()
                #limb.rotate(limb.speed*limb.direction)
        updateAll(data)
    #set mode functionality test



def redrawAll(canvas, data):
    #drawGrid(canvas,data)

    data.testLimbButton.draw(canvas)
    data.playButton.draw(canvas)
    
    drawAllLimbs(canvas,data)
    
    if data.selectedLimb != None:
        drawMenu(canvas,data)
        data.switchButton.draw(canvas)
        for slider in data.sliders:
            slider.draw(canvas,data)
        data.EventMenu.draw(canvas,data)


    #data.radialDialTest.draw(canvas)

    # data.rotationSlider.draw(canvas,data)
    # data.speedSlider.draw(canvas,data)
    
####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mouseReleasedWrapper(event,data,canvas):
        mouseReleased(event,data,canvas)

    def movedWrapper(event,data,canvas):
        mouseMoved(event,data)
        redrawAllWrapper(canvas, data)

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 1000# milliseconds
    root = Tk()

    init(data)

    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack(side = LEFT)

    root.bind("<Motion>", lambda event:
                            movedWrapper(event,data,canvas))
    # root.bind("<Motion>", lambda event:
    #                         movedWrapper(event, data))

    root.bind("<ButtonRelease-1>", lambda event:
                                    mouseReleased(event,data,canvas))
    
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))

    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 800)
#run(1000, 500)