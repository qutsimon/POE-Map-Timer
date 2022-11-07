import tkinter
from tkinter import messagebox
import os
import pickle
import data


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


#Also needs rename
class Category_gui:
    def __init__(self, master):
        self.master = master
        master.geometry("+220+150")

        self.list = tkinter.Listbox(master, height=10, selectmode='browse')
        self.enter = tkinter.Entry(master)
        self.add = tkinter.Button(master, text="Add", command = self.add_cat)
        self.remove= tkinter.Button(master, text="Remove", command = self.remove_cat)
    
        self.list.grid(row=0, column = 0, columnspan=2)
        self.enter.grid(row=1, column = 0, columnspan=2)
        self.add.grid(row=2, column=0)
        self.remove.grid(row=2, column=1)

        self.refresh_listbox()

    def add_cat(self):
        if self.enter.get() == '':
            messagebox.showerror(title="Error", message="Please enter a name")
            return
        name = self.enter.get()+".pkl"
        dir = os.getcwd()+'/data/'
        data_dir_list = os.listdir(dir)
        if name in data_dir_list:
            messagebox.showerror(title="Error", message="This category already exists")
            return
        else:
            with open(dir+name, 'wb') as f:
                pickle.dump(data.Data(self.enter.get()), f)
        self.refresh_listbox()
        

    #this also needs to delete data? Also probably needs a warning
    def remove_cat(self):
        print(self.list.curselection())
        print(self.list.get(self.list.curselection()))
    
    def refresh_listbox(self):
        self.list.delete(0,tkinter.END)
        counter = 0
        for file in os.listdir(os.getcwd()+'/data/'):
            name = file.split('.')
            self.list.insert(counter, name[0])
            counter += 1


