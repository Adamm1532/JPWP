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

        self.Mail_Text = ctk.CTkLabel(self.backgroundFrame,
                                     text="Podaj swól e-mail:",
                                     font=("Arial", 20),
                                     text_color=glb.color_magenta)
        self.Mail_Text.place(relx=self.Bank_x+0.05, rely=0.48, anchor="se")

        self.Entry_Mail = ctk.CTkEntry(self.backgroundFrame,
                                       placeholder_text="np. cos@tam.pl",
                                       fg_color="white",
                                       width=300, height=30,
                                       placeholder_text_color="gray",
                                       text_color="black")
        self.Entry_Mail.place(relx=self.Bank_x, rely=0.5, anchor="center")



Label().mainloop()