from HelperFunctions import *
from Button import *

class ToggleButton(Button):
    def __init__(self,name,x,y,width,height):
        super().__init__(name,x,y,width,height)

    def draw(self,canvas):
        # if self.active:
        #     pass
        # else:
        round_rectangle(self.x,self.y,
            self.x+self.width,self.y+self.height,canvas, radius=30, fill="grey")
        canvas.create_text(self.x+self.width/2,self.y+self.height/2,
            text=self.name, fill="black", font="Helvetica 14")
