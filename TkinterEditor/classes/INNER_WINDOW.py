from tkinter import*
class Inner_window:
    def __init__(self,root,x,y):
        self.window = Toplevel(root)
        self.x=x
        self.y=y
        self.window.transient(root) #Keeps sub window on top of root
        root.bind('<Configure>', self.move_root)
        self.window.bind('<Configure>', self.move_window)
        self.window.geometry("+{0}+{1}".format(self.x,self.y))
    def move_root(self,event):
        self.window.geometry("+{0}+{1}".format(event.x+self.x,event.y+self.y))
    def move_window(self,event):
        event.widget.geometry("+{0}+{1}".format(event.x, event.y))

