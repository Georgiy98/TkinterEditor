from tkinter import *
from classes.SCROLL_FRAME import *
from classes.BOOK import *
from classes.PROJECT import *
import public_data as p
import os,os.path,constructor
#whole project window
def run(name,way):
    def start():
        p.window.content["__init__"].start_by_frame(p.constructor_frame)
    def read(event):
        current_text=Text(book.box)
        if not event.widget["text"] in book.pages.keys():
            book.add_page({event.widget["text"]: current_text})
        p.window.content["__init__"].start_by_frame(p.constructor_frame)
        text = p.window.content["__init__"].get_text()
        p.window.content["__init__"].close_window()
        current_text.delete("0.0",END)
        current_text.insert(END,text)
        with open("projects\\__init__.py", "w") as f:
            f.write(text)
    def save():
        for i in p.window.content.keys():
            p.window.content[i].start_by_frame(p.constructor_frame)
            text = p.window.content[i].get_text()
            p.window.content[i].close_window()
            with open(way+"\\"+i+".py", "w") as f:
                f.write(text)
    def call_constructor(event):
        print("way = %s, name = %s"%(way,name))
        constructor.run(book.box,"projects","current_example666",root)

    root = Tk()
    p.window= project(way+"\\")
    root.state("zoomed")
    root.title("Tkinter Editor"+150*" "+name)
    root.config(bg="#DDDDFF")
    menu_panel = Frame(root,width=root.winfo_screenwidth(),height=20,bg="#6666AA")
    menu_panel.place(x=0,y=22)
    menu = Frame(root,width=root.winfo_screenwidth(),height=20,bg="#6666AA")
    menu.place(x=0,y=0)

    folder_image    =PhotoImage(file="images\\folder.gif")
    file_py_image   =PhotoImage(file="images\\file_py.gif")
    txt_image       =PhotoImage(file="images\\file_txt.gif")
    unknown_image   =PhotoImage(file="images\\file_unknown.gif")

    catalog = Scroll_frame(root,root.maxsize()[0]-250,44,250,300,"#BBBBDD")
    catalog.put()
    t=0
    for i in os.listdir(way+"\\"):
        h=Button(catalog.field,text=i,font = "Times 8",relief = RIDGE,width=30,bg="#CCCCDD")
        h.place(x=40,y=t*20)

        if (os.path.isdir(way+"\\"+i)):
            Label(catalog.field,image=folder_image,relief = FLAT,bg="#99CC00").place(x=20,y=t*20)
        elif (i[-3:]==".py"):
            h.bind("<1>",read)
            Label(catalog.field,image=file_py_image,relief = FLAT,bg="#99CC99").place(x=20,y=t*20)
        elif (i[-4:]==".txt"):
            h.bind("<1>",read)
            Label(catalog.field,image=txt_image,relief = FLAT,bg="#99CC00").place(x=20,y=t*20)
        else:
            Label(catalog.field,image=unknown_image,relief = FLAT,bg="#99CC00").place(x=20,y=t*20)
        t+=1
    catalog.create_yscroll(230,1,230,177,
                           Button(catalog.field,text=(chr(708)+"\n")*5,font="Arial 11 bold",width=1,bg="#8888AA"),
                           Button(catalog.field,text=("\n"+chr(709))*5,font="Arial 11 bold",width=1,bg="#8888AA")
                           )
    catalog.create_hide_but(0,20,Button(catalog.field,text=">\n"*15+">",font="Arial 11 bold",width=1,bg="#8888AA"))
    catalog.create_expand_but(100,0,Button(menu_panel,text="Catalog",font="Arial 8 bold",bg="#8888FF"))
    catalog.create_move_but(0,0,Button(catalog.field,text="+",font="Arial 11 bold",width=1,bg="#8888AA"))

    book = Book(root,"horizontal",
     Description(100,43,root.winfo_screenwidth()-450,25,"#6666AA"),
     Description(0,70,root.winfo_screenwidth()-250,root.winfo_screenheight()-140,"#DDDDFF"),
     Description(root.winfo_screenwidth()-350, 42, 10, 1, "#222266", ">"*8,font = "Arial 11 bold"),
     Description(0,42,10,1,"#222266","<"*8,font = "Arial 11 bold"),
     Description(height=1,bg="#444499")
     )
    Button(menu,text="Run",bg="#BBBBEE",fg="#111155",font="Arial 9 bold",command=start).place(x=200,y=0)
    Button(menu,text="Save",bg="#BBBBEE",fg="#111155",font="Arial 9 bold",command=save).place(x=700,y=0)
    ttt = Button(menu,text="Constructor",bg="#BBBBEE",fg="#111155",font="Arial 9 bold")
    ttt.place(x=500,y=0)
    ttt.bind("<1>",call_constructor)
    constructor.run(book.box,way,name,root)

    root.mainloop()
#run("qwe","D:\projects")
