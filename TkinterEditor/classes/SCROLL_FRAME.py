from tkinter import *
from classes.Timer import *
class Scroll_frame:
    field       ="" #Панель, на которой размещены остальные виджеты
    up_but      ="" #Верхняя кнопка для проматывания
    down_but    ="" #Нижняя кнопка для проматывания
    right_but   ="" #Правая кнопка для проматывания
    left_but    ="" #Левая кнопка для проматывания
    dist_x      ="" #Расстояние,на которое следует проматывать (в длину)
    dist_y      ="" #Расстояние,на которое следует проматывать (в высоту)
    up_line     ="" #Верхний предел
    down_line   ="" #Нижний предел
    right_line  ="" #Правый предел
    left_line   ="" #Левый предел
    exception   =[] #Список обьектов, которые не следует проматывать
    hide_but    ="" #Кнопка сворачивания
    expand_but  ="" #Кнопка развертывания
    move_but    ="" #Кнопка перемещения
    current_x   =""
    current_y   =""
    need_move   =True
    res_x_but   =""
    res_y_but   =""
    area        =""
    def down(self,event):
        do=False
        for i in self.field.place_slaves():
            if (int(i.place_info()["y"])>=self.field["height"]-self.dist_y-1):
                do=True
                break
        #do=True
        if do:
            for i in self.field.place_slaves():
                if (not i in self.exception):
                    i.place(x=int(i.place_info()["x"]),y=int(i.place_info()["y"])-self.dist_y)
    
    def up(self,event):
        do=False
        for i in self.field.place_slaves():
            if (int(i.place_info()["y"])<=-1):
                do=True
                break
        #do=True
        if do:
            for i in self.field.place_slaves():
                if (not i in self.exception):
                    i.place(x=int(i.place_info()["x"]),y=int(i.place_info()["y"])+self.dist_y)

    def left(self,event):
        do=False
        for i in self.field.place_slaves():
            if (int(i.place_info()["x"])>=self.right_line):
                do=True
                break
        #do=True
        if do:
            for i in self.field.place_slaves():
                if (not i in self.exception):
                    i.place(x=int(i.place_info()["x"])-self.dist_x,y=int(i.place_info()["y"]))

    def right(self,event):
        do=False
        for i in self.field.place_slaves():
            if (int(i.place_info()["x"])<=-1):
                do=True
                break
        #do=True
        if do:
            for i in self.field.place_slaves():
                if (not i in self.exception):
                    i.place(x=int(i.place_info()["x"])+self.dist_x,y=int(i.place_info()["y"]))
    
    def __init__(self,root,f_x=0,f_y=0,f_width=100,f_height=100,f_bg="#222222"):
        self.field=Frame(root,width=f_width,height=f_height,bg=f_bg)
        #self.field.place(x=f_x,y=f_y)
        self.current_x=f_x
        self.current_y=f_y

    def put(self):
        self.field.place(x=self.current_x,y=self.current_y)
        
    def add_exception(self,b):
        self.exception.append(b)
    
    def create_yscroll(self,x1,y1,x2,y2,up_b,down_b,dist_y=40):
        self.dist_y=dist_y

        self.up_but=up_b
        self.up_but.bind("<1>",self.up)
        self.up_but.place(x=x1,y=y1)

        self.down_but=down_b
        self.down_but.bind("<1>",self.down)
        self.down_but.place(x=x2,y=y2)
        self.exception.append(self.up_but)
        self.exception.append(self.down_but)

    def create_xscroll(self,x1,y1,x2,y2,r_but,l_but,dist_x=40,left_line = -1, right_line = 666666):
        self.dist_x=dist_x
        self.left_line=left_line
        self.right_line=right_line
        if self.right_line == 666666:
            self.right_line = self.field["width"]-self.dist_x-1
        #self.field["width"]-self.dist_x-1

        self.right_but=r_but
        self.right_but.bind("<1>",self.right)
        self.right_but.place(x=x1,y=y1)

        self.left_but=l_but
        self.left_but.bind("<1>",self.left)
        self.left_but.place(x=x2,y=y2)

        self.exception.append(self.right_but)
        self.exception.append(self.left_but)
    def hide(self,event):
        self.expand_but.place(x=self.xe,y=self.ye)
        self.field.place(x=5000,y=5000)
    def create_hide_but(self,x,y,but):
        self.hide_but=but
        self.hide_but.place(x=x,y=y)
        self.hide_but.bind("<1>",self.hide)
        self.exception.append(self.hide_but)
    def expand(self,event):
        self.expand_but.place(x=5000,y=5000)
        self.field.place(x=self.current_x,y=self.current_y)
    def create_expand_but(self,x,y,but):
        self.expand_but=but
        self.expand_but.bind("<1>",self.expand)
        self.xe=x
        self.ye=y
        self.exception.append(self.expand_but)

    def h_move(self):
        x1=self.field.master.winfo_pointerx()-10
        y1=self.field.master.winfo_pointery()-35
        self.field.place(x=x1,y=y1)


        #return self.need_move
    def move(self,event):
        if self.need_move:
            self.timer.Start()
        else:
            self.timer.Stop()
            self.current_x=self.field.winfo_rootx()
            self.current_y=self.field.winfo_rooty()-22
        self.need_move= not self.need_move

    def create_move_but(self,x,y,but):
        #self.area=area
        self.timer=Timer(do=self.h_move,Interval=0.01)
        self.move_but=but
        self.move_but.place(x=x,y=y)
        self.move_but.bind("<1>",self.move)
        self.exception.append(self.move_but)
    def h_resize_height(self):
        if self.field["height"]!=500:
            self.field["height"]=500
    def resize_width(self,event):
        pass
    def create_resize(self,height_but=NONE,y=0,width_but=NONE,x=0):
        if height_but != NONE:
            height_but.place(x=0,y=y)
            height_but.bind("<1>",self.resize_width)
            self.exception.append(height_but)
    def clear(self):
        for i in self.field.place_slaves():
            if not i in self.exception:
                i.destroy()
                del i



