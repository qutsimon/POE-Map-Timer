"""
To DO
- Config files for hotkeys
- Hotkeys settings frame?
- Keep on top always
- counter for multiple different categories/maps - also gui for these
- history with the ability to delete
- averaging/graphing, data in the different categories
- storage of category data - pickle? database? csv?
- buttons corresponding to start, stop and pause or even labels but 
they indicate at the action that timer is currently taking
"""
import gui
from tkinter import Tk
import timer

root = Tk()
guis = gui.Main_gui(root)
timer = timer.Timer(set())

guis.timer_text(root, timer)

#Hotkey binds - this later in config file
root.bind('<Control-Shift-S>', timer.start_timer)
root.bind('<Control-Shift-D>', timer.time_stop)
root.bind('<Control-Shift-X>', timer.timer_pause)
root.bind('<Control-Shift-Z>', root.quit)

root.mainloop()
