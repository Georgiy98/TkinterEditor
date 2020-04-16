from tkinter import *
import time
import threading

#-------------------------------------------------------------------------------------------------------------
# Виджет,содержащий вкладки с возможностью переключения панелей
#-------------------------------------------------------------------------------------------------------------

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


#-------------------------------------------------------------------------------------------------------------
# Вспомогательный класс для описания виджетов
#-------------------------------------------------------------------------------------------------------------

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


#-------------------------------------------------------------------------------------------------------------
# Выпадающий список
#-------------------------------------------------------------------------------------------------------------

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


#-------------------------------------------------------------------------------------------------------------
# Виджет,который способен проматывать свои элементы
#-------------------------------------------------------------------------------------------------------------

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


#-------------------------------------------------------------------------------------------------------------
# Класс, позволяющий циклично запускать необходимую функцию в отдельном потоке
#-------------------------------------------------------------------------------------------------------------

class Timer():
    do          =""
    Interval    =""
    Enabled     =""
    Proccess    =""

    def __init__(self,do,Interval,event=None):
        self.Interval=Interval
        self.do=do
        self.Enabled=False
        self.Proccess=True

    def Tick(self,event=None):
        self.Enabled=True
        while self.Enabled:
            self.do()
            time.sleep(self.Interval)

    def Tick_pause(self,event=None):
        self.Enabled=True
        while self.Enabled:
            if self.Proccess:
                self.do()
            time.sleep(self.Interval)

    def Start(self,pause=False,event=None):
        if not self.Enabled:
            if pause:
                self.Proccess=True
                t = threading.Thread(target=self.Tick_pause)
            else:
                t = threading.Thread(target=self.Tick)
            t.start()

    def Pause(self,event=None):
        self.Proccess=False

    def Continue(self,event=None):
        self.Proccess=True

    def Stop(self,event=None):
        self.Enabled=False


