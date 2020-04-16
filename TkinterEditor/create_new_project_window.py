from tkinter import *
from tkinter.messagebox import *
import dialog_way,Develop_window,os
way=0
neighbours=0
def run(root):
    global way
    def create(Name,Way):
        Way=Way+"\\"+Name
        os.mkdir(Way)
        with open("list_projects.txt","a") as f:
            f.write(Name+"\n"+Way+"\n")
        with open(Way+"\\__init__.py","w") as f:
            f.write("""from tkinter import *
root=Tk()
root.mainloop()
""")
        window.destroy()
        root.destroy()
        Develop_window.run(Name,Way)
    def save():
        dialog_way.run(window,False)
    def do():
        error_name=False
        for i in name.get():
            if not (ord(i) in range(65,91) or ord(i) in range(97,123) or i in range(1040,1109) or i in "1234567890_-+ "):
                error_name = True
                break
        if ((name.get() in neighbours) or
                (len(name.get())==0) or error_name):
            showinfo("Tkinter Editor - Error", "Unaviable name of project!\nName can consists of:\n - russian letters\n -english letters\n - digits\n"
                        " - whitespace и symbols: _ - +\nDirectory cannot have other folders with the same name.")
            window.focus_set()
        else:
            create(name.get(),way.get())
    window=Toplevel(root)
    window.title("Tkinter Editor"+" "*10+"Creating of new project")
    window.geometry("600x400+200+80")
    window.config(bg="#666677")
    window.grab_set()
    window.focus_set()
    Label(window,text="Name of project",font="Arial 15 bold", fg="#CCCCCC", bg=window["bg"]).place(x=200,y=20)
    name=Entry(window,bg="#AAAABB",font="Arial 13",width=50,fg="#444444")
    name.place(x=70,y=50)
    Label(window,text="Location of project",font="Arial 15 bold", fg="#CCCCCC", bg=window["bg"]).place(x=200,y=120)
    way=Entry(window,bg="#AAAABB",font="Arial 13",width=50,fg="#444444")
    way.place(x=70,y=150)
    Button(window,text="Choose\nfolder",command=save,bg="#AAAABB",font="Arial 13",fg="#444444").place(x=460,y=180)
    Button(window,text="Continue",font="Arial 15 bold", fg="#CCCCCC", bg=window["bg"],relief=FLAT,command=do).place(x=260,y=350)
    window.wait_window()
    window.mainloop()
def get_way(text,nh):
    global neighbours
    way.delete(0,END)
    way.insert(0,text)
    neighbours=nh
