import tkinter
from UI.category_gui import Category_gui


class Main_gui:
    def __init__(self, master):
        self.master = master
        #Random off set at this moment
        master.geometry("200x100+20+50")

        self.label = tkinter.Label(master, text="Hello test")
        self.label.pack()

        self.cat_button = tkinter.Button(master, text="Settings", command=self.show_cat)
        self.cat_button.pack()

        self.close_button = tkinter.Button(master, text="close", command=lambda: master.quit())
        self.close_button.pack()

        master.attributes('-topmost','true')
        master.attributes('-alpha','0.9')
        
        #Removes window title bar
        master.overrideredirect(True)
        

    '''
    root:
    timer:
    Returns: None
    '''
    def timer_text(self, root, timer):
        self.label.config(text=str(timer.return_dif()))
        root.after(100, self.timer_text, root, timer)

    def show_cat(self):
        self.newWindow = tkinter.Toplevel(self.master)
        self.app = Category_gui(self.newWindow)




