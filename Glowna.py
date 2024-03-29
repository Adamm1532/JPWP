import time
from threading import Thread
import PIL as pil
import customtkinter as ctk
import Globalne as glb


class Glowna(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bank Login")
        self.geometry("420x740+700+20")
        self.Frame_x=0
        self.backgroundFrame = ctk.CTkFrame(self,
                                            fg_color=glb.color_background,
                                            border_color=glb.color_background,
                                            width=420, height=740)
        self.backgroundFrame.place(relx=self.Frame_x, rely=0, anchor="nw")




    def destruction(self):
       self.after(2500, self.destroy)

Glowna().mainloop()
#import Bank_Ustawienia