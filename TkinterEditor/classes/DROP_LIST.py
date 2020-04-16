from tkinter import*
from classes.SCROLL_FRAME import *
class Drop_list:
    def __init__(self,root,value_label,drop_but,field,button,but_width,height,values):
        self.but_width      = but_width
        self.status         = False
        self.value_label    = value_label
        self.drop_but       = drop_but
        self.drop_but.bind("<1>",self.click)
        self.field          = field
        self.buttons        = []
        self.height         = height
        for i in range(len(values)):
            for u in button.keys():
                try:
                    but=Button(self.field.field)
                    but[u]=button[u]
                    but["text"] = values[i]
                    but.place(x=1,y=2+(but.winfo_reqheight()+2)*i,width = but_width)
                    but.bind("<1>",self.choose)
                    self.buttons.append(but)
                except:
                    pass
        self.field.field["height"]=(self.buttons[0].winfo_reqheight()+2)*self.height

    def click(self,event):
        self.status = not self.status
        if self.status:
            self.field.field.place(x=self.field.current_x,y=self.field.current_y,height = (self.buttons[0].winfo_reqheight()+2)*self.height)
            self.field.field.tkraise()
        else:
            self.field.field.place(x=10000,y=10000)
    def choose(self,event):
        self.value_label["text"]=event.widget["text"]
        self.field.field.place(x=10000,y=10000)
        self.status = False
    def place(self,x,y):
        self.drop_but.place(x=x+self.but_width+1,y=y-1)
        self.value_label.place(x=x,y=y,width = self.but_width)
        self.field.current_x = x
        self.field.current_y = y + self.value_label.winfo_reqheight()
    def create_yscroll(self,up_b = 666666,down_b = 666666,dist_y=40):
        if up_b == 666666:
            up_b=Button(self.field.field,text=(chr(708)+"\n")*2)
        if down_b == 666666:
            down_b=Button(self.field.field,text=(chr(709)+"\n")*2)
        x1=self.value_label.place_info()["width"]
        x2=self.value_label.place_info()["width"]
        y1=0
        y2=(self.buttons[0].winfo_reqheight()+2)*self.height-down_b.winfo_reqheight()
        self.field.create_yscroll(x1,y1,x2,y2,up_b,down_b,dist_y)
    def get_value(self):
        return self.value_label["text"]
    def set_value(self,value):
        self.value_label["text"] = value

