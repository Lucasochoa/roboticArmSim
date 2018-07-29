class Button(object):
    buttons = []
    def __init__(self,name,x,y,width,height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        Button.buttons.append(self)

    def clicked(self,event,data):
        if event.x > self.x and event.x < self.x+self.width\
            and event.y > self.y and event.y < self.y+self.height:
                print('button',self.name,'clicked')
                return True
        return False

    def draw(self,canvas):
        canvas.create_rectangle(self.x,self.y,self.x+self.width,
            self.y + self.height, fill = 'red')

