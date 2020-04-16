import os,classes.WINDOW
class project:
    # strucure: [root1,root2,root3..]
    def __init__(self,way):
        self.way = way
        self.content = dict()
        for i in os.listdir(way):
            if i[-3:] == ".py":
                try:
                    self.content[i[:-3]]=classes.WINDOW.Window(way+i)
                except:
                    self.content[i[:-3]]=0

