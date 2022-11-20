import UI.main_gui as main_gui
from tkinter import Tk
import models.timer as timer

root = Tk()
guis = main_gui.Main_gui(root)
timer = timer.Timer(set())

guis.timer_text(root, timer)

#read config file here

#Hotkey binds - this later in config file
root.bind('<Control-Shift-S>', timer.start_timer)
root.bind('<Control-Shift-D>', timer.time_stop)
root.bind('<Control-Shift-X>', timer.timer_pause)
root.bind('<Control-Shift-Z>', root.quit)

root.mainloop()
