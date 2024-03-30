import time
from threading import Thread
import PIL as pil
from PIL import Image, ImageTk
import customtkinter as ctk
import Globalne as glb
from datetime import datetime
import os

class Profil(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Profil")
        self.geometry("420x740+700+20")

        self.background_frame = ctk.CTkFrame(self,
                                             fg_color=glb.color_background,
                                             border_color=glb.color_background,
                                             width=420, height=740)
        self.background_frame.place(relx=0, rely=0, anchor="nw")


        

        # Wywołanie funkcji
        self.profile_img = ctk.CTkImage(dark_image=pil.Image.open("uzytkownik.png"), size=(200, 200))
        self.Profile_Button = ctk.CTkButton(self.background_frame, image=self.profile_img, text="",
                                         width=50, height=50,
                                         fg_color=glb.color_background,
                                         
                                         command=self.my_upload,
                                         hover_color=glb.color_background)
        self.Profile_Button.place(relx=0.5, rely=0.5, anchor="center")  



    def my_upload(self):
        global filename

        # Użytkownik wybiera plik obrazu
        f_types = [('All files', '*.*'), ('JPG', '*.jpg'), ('PNG', '*.png')]
        filename = ctk.filedialog.askopenfilename(filetypes=f_types)
        image_pil = Image.open(filename)
        # Otwórz wybrany plik obrazu i przypisz go do zmiennej profile_img
        self.profile_img = ctk.CTkImage(dark_image=Image.open(filename), size=(200, 200))
        
        # Zaktualizuj obrazek przycisku
        self.Profile_Button.configure(image=self.profile_img)


        output_filename = "uzytkownik.png"
        #image_pil = self.profile_img._light_image # Pobierz obraz PIL z obiektu CTkImage
        image_pil.save(output_filename, overwrite=True)  # Zapisz obraz PIL




Profil().mainloop()        