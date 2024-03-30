import time
from threading import Thread
import PIL as pil
from PIL import Image, ImageTk, ImageOps
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


        
        self.mask = Image.open('mask.png').convert('L')
        im = Image.open('uzytkownik.png')

        output = ImageOps.fit(im, self.mask.size, centering=(0.5, 0.5))
        output.putalpha(self.mask)

        output.save('uzytkownik.png')
        # Wywołanie funkcji
        self.profile_img = ctk.CTkImage(dark_image=pil.Image.open("uzytkownik.png"), size=(200, 200))
        self.Profile_Button = ctk.CTkButton(self.background_frame, image=self.profile_img, text="",
                                         width=200, height=200,
                                         fg_color=glb.color_background,
                                         
                                         command=self.my_upload,
                                         hover_color=glb.color_background,
                                         corner_radius=100)
        self.Profile_Button.place(relx=0.5, rely=0.3, anchor="center")  



    def my_upload(self):
        global filename

        # Użytkownik wybiera plik obrazu
        f_types = [('All files', '*.*'), ('JPG', '*.jpg'), ('PNG', '*.png')]
        filename = ctk.filedialog.askopenfilename(filetypes=f_types)
        
        # Otwórz wybrany plik obrazu i przypisz go do zmiennej profile_img


        image_pil = Image.open(filename)
        output_filename = "uzytkownik.png"
        #image_pil = self.profile_img._light_image # Pobierz obraz PIL z obiektu CTkImage
        image_pil.save(output_filename, overwrite=True)  # Zapisz obraz PIL
        im = Image.open('uzytkownik.png')

        output = ImageOps.fit(im, self.mask.size, centering=(0.5, 0.5))
        output.putalpha(self.mask)

        output.save('uzytkownik.png')
        self.profile_img = ctk.CTkImage(dark_image=Image.open("uzytkownik.png"), size=(200, 200))
        
        # Zaktualizuj obrazek przycisku
        self.Profile_Button.configure(image=self.profile_img)



Profil().mainloop()        