import os
import pickle
import tkinter
from tkinter import messagebox
import models.data as data

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

        #scrollbar
        scrollbar = tkinter.Scrollbar(master, orient="vertical", command=self.list.yview)
        scrollbar.grid(row=0, column=2, sticky='NS')

        self.list.config(yscrollcommand=scrollbar.set)

        #Make non-resizable
        master.resizable(False, False)

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
        

    def remove_cat(self):
        file_name = self.list.get(self.list.curselection()) + '.pkl'
        data_dir = os.getcwd()+'/data/'
        print(data_dir)
        if file_name in os.listdir(data_dir):
            answer = messagebox.askyesno(title="Confirmation", message="Are you sure you want to delete this file?")
            if answer:
                os.remove(data_dir+file_name)
                self.refresh_listbox()
        else:
            messagebox.showerror(title="Error", message="File not found")
            self.refresh_listbox()

    
    def refresh_listbox(self):
        self.list.delete(0,tkinter.END)
        counter = 0
        for file in os.listdir(os.getcwd()+'/data/'):
            name = file.split('.')
            self.list.insert(counter, name[0])
            counter += 1
