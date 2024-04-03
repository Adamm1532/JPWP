import time
from threading import Thread
import PIL as pil
import customtkinter as ctk
import Globalne as glb

class Label(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Profil")
        self.geometry("420x740+700+20")
        self.Bank_x = 0.5


        self.backgroundFrame = ctk.CTkFrame(self,
                                            fg_color=glb.color_background,
                                            border_color=glb.color_background,
                                            width=420, height=740)
        self.backgroundFrame.place(relx=0, rely=0, anchor="nw")





Label().mainloop()