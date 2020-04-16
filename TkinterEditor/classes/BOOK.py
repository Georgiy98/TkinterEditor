from tkinter import *
from classes.SCROLL_FRAME import *
class Book:
    pages           =dict()
    page_but_style  =""
    box             =""
    pages_container =""
    align           =""
    x_limit         =0
    y_limit         =0
    #page: [name,frame]
    def go(self,event):
        for i in self.box.place_slaves():
            i.place(x=5000,y=5000)
        self.pages[event.widget["text"]].place(x=0,y=0)

    def __init__(self,root,align,up_cont,box,left_up_but,right_down_but,page_but_style):
        self.box = Frame(root,width = box.width,height = box.height, bg= box.bg )
        self.box.place(x=box.x,y=box.y)
        self.page_but_style = page_but_style
        self.align = align
        self.pages_container = Scroll_frame(root,
                up_cont.x,up_cont.y,up_cont.width,up_cont.height,up_cont.bg)
        self.pages_container.put()
        if align == "horizontal":
            self.pages_container.create_xscroll(right_down_but.x,right_down_but.y,left_up_but.x,left_up_but.y,
                Button(root,width = right_down_but.width,height = right_down_but.height,text = right_down_but.text,bg = right_down_but.bg,font = right_down_but.font),
                Button(root,width = left_up_but.width,height = left_up_but.height,text = left_up_but.text,bg = left_up_but.bg,font = left_up_but.font),50)
        elif align == "vertical":
            self.pages_container.create_yscroll(right_down_but.x,right_down_but.y,left_up_but.x,left_up_but.y,
                Button(root,width = right_down_but.width,height = right_down_but.height,text = right_down_but.text,bg = right_down_but.bg,font = right_down_but.font),
                Button(root,width = left_up_but.width,height = left_up_but.height,text = left_up_but.text,bg = left_up_but.bg,font = left_up_but.font),50)
    def out(self,event):
        for i in self.pages_container.field.place_slaves():
            if  not i in self.pages_container.exception:
                i.destroy()
        self.pages[event.widget.target].destroy()
        self.x_limit=0
        self.pages.pop(event.widget.target)
        self.add_page(self.pages)
    def add_page(self,pages):
        if self.align == "horizontal":
            for i in pages.keys():
                t=Button(self.pages_container.field,text=i,bg=self.page_but_style.bg,height=self.page_but_style.height)
                t.bind("<1>",self.go)
                t.place(x=self.x_limit,y=1)
                self.x_limit+=t.winfo_reqwidth()
                h=Button(self.pages_container.field,text="X\n\n",font = "Arial 5 bold")
                h.target = i
                h.bind("<1>",self.out)
                h.place(x=self.x_limit,y=1)
                self.x_limit+=h.winfo_reqwidth()
                self.pages[i]=pages[i]
        else:
            for i in pages.keys():
                Button(self.pages_container.field,text=i).place()
class Description:
    def __init__(self,x=0,y=0,width=10,height=1,bg="#FFFFFF",text="Example",font = "Arial 10",relief = RAISED):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.bg=bg
        self.text=text
        self.font=font
        self.relief=relief

#w= {"red": Frame(book.box,width=500,height=200,bg="red"),"green": Frame(book.box,width=500,height=200,bg="green"),"blue": Frame(book.box,width=500,height=200,bg="blue")}

