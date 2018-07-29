from AddEventButton import *
from HelperFunctions import *
from RotationEvent import *
from Slider import *

class EventMenu(object):
    def __init__(self,name,x,y,data):
        self.name = name
        self.x = x
        self.y = y
        self.rowHeight = data.height/15
        self.active = False
        self.addButton = AddEventButton("addEvent",self.x,self.y,self.rowHeight,
            self.rowHeight)
        self.addMode = False

        self.setupEvents(data)
        
        self.selectedEvent = None
        self.sliders = []
        self.sliders.extend([Slider("Event Speed",data.width*(3/5),
            data.height/2,100,20,0,100),Slider("Event Duration",
            data.width*(3/5),data.height/2+50,100,20,0,100)])

    def setupEvents(self,data):
        self.eventButtons = []
        self.eventButtons.extend([\
            AddRotationEventButton("Clockwise",data.width*(13/20),300,150,50),\
            AddRotationEventButton("Counter Clockwise",data.width*(13/20),\
            400,150,50),\
            AddRotationEventButton("Stop",data.width*(13/20),500,150,50)])

    #deletes selected table if delete button is pressed     
    def colidedWithDelete(self,event,data,row,x,y):
        if distance(x,y,event.x,event.y) < self.rowHeight*(3/5):
            data.selectedLimb.events.pop(row)
            data.selectedLimb.updateEvents()
            return True
        return False
            

    def findRowAndUpdate(self,event,data):
        if data.selectedLimb != None:
            selectedRow = None
            for row in range(len(data.selectedLimb.events)):
                if event.x > self.x and event.y > self.y+self.rowHeight*(row+1)\
                and event.x < data.width and\
                event.y < self.y+self.rowHeight*(row+2):

                    if self.colidedWithDelete(event,data,row,
                        data.width-self.rowHeight/2,
                        self.y+self.rowHeight*(row+1)+self.rowHeight/2):
                            break
                    data.selectedLimb.events[row].selected = True
                    self.selectedEvent = data.selectedLimb.events[row]
                    selectedRow = row+1
                else:
                    data.selectedLimb.events[row].selected = False
            if selectedRow == None:
                self.selectedEvent = None
            return selectedRow

    def sliderLogic(self,event):
        for slider in self.sliders:
            if slider.mouseClickedDown(event):
                return True
        return False

    def eventButtonLogic(self,event,data):
        for button in self.eventButtons:
            if button.clicked(event,data):
                if button.name == "Clockwise":
                    data.selectedLimb.addEvent(RotationEvent("clockwise",1,5))
                    return True
                elif button.name == "Counter Clockwise":
                    data.selectedLimb.addEvent(\
                    RotationEvent("counter clockwise",-1,5))
                    return True
                elif button.name == "Stop":
                    data.selectedLimb.addEvent(\
                    RotationEvent("stop",0,5))
                    return True
        return False

    def clicked(self,event,data):
        #sliderLogic                    
        if self.sliderLogic(event):return True

        self.findRowAndUpdate(event,data)
        
        self.addMode = self.addButton.clicked(event,data)


        if self.eventButtonLogic(event,data): return True
        
        if event.x > self.x and event.y > self.y:
            #self.active = True
            print("clicked event from Event Menu")
            return True
        else:
            #self.active = False
            return False

    def mouseMoved(self,event,data):
        if self.selectedEvent != None:
            for slider in self.sliders:
                slider.mouseMoved(event,data)

    def mouseReleased(self,event):
        if self.selectedEvent != None:
            for slider in self.sliders:
                slider.mouseReleased(event)

    def draw(self,canvas,data):
        if data.selectedLimb != None:
            canvas.create_rectangle(self.x,self.y,data.width,data.height,
                fill = "grey")
            self.drawEvents(canvas,data)
            self.drawHeader(canvas,data)
            self.drawLabels(canvas,data)
            self.addButton.draw(canvas,data)
            if self.addMode:
                for button in self.eventButtons:
                    button.draw(canvas,data)
                #canvas.create_rectangle(self.x,self.y)
            if self.selectedEvent != None:
                self.drawSliders(canvas,data)
            if self.active:
                canvas.create_rectangle(self.x,self.y,data.width,
                self.y+self.rowHeight,width = 3,fill = "red")

    def drawSliders(self,canvas,data):
        for slider in self.sliders:
            slider.draw(canvas,data)

    def drawHeader(self,canvas,data):
        canvas.create_rectangle(self.x,self.y,data.width,
            self.y+self.rowHeight,width = 3)
        halfX = (data.width - self.x)/2
        halfY = self.rowHeight/2
        canvas.create_text(self.x+(data.width-self.x)*(3/5),self.y+self.rowHeight/2,
            text = "Add Event",fill = "black",font = "Helvetica 16 bold")

    def drawLabels(self,canvas,data):
        for row in range(len(data.selectedLimb.events)):
            halfX = (data.width - self.x)/2
            halfY = self.rowHeight/2
            canvas.create_text(self.x+halfX,self.y+self.rowHeight*(row+1)+halfY,
                text=data.selectedLimb.events[row].name,fill="black",
                font="Helvetica 16 bold")

    def drawEvents(self,canvas,data):
        for row in range(len(data.selectedLimb.events)):
            color = "grey"
            if data.selectedLimb.events[row].active:
                color = "blue"
            if data.selectedLimb.events[row].selected:
                color = "green"

            canvas.create_rectangle(self.x,self.y+self.rowHeight*(row+1),
                                    data.width,self.y+self.rowHeight*(row+2),
                                    width = 1,fill = color)
            #draws delete button
            padding = self.rowHeight/5
            canvas.create_oval(data.width-self.rowHeight+padding,
                               self.y+self.rowHeight*(row+1)+padding,
                               data.width-padding,
                               self.y+self.rowHeight*(row+2)-padding,
                               fill = "red",width = 2)
            canvas.create_line(data.width-self.rowHeight+padding*1.5,
                               self.y+self.rowHeight*(row+1)+self.rowHeight/2,
                               data.width-padding*1.5,
                               self.y+self.rowHeight*(row+1)+self.rowHeight/2)

