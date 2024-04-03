import PIL as pil
from PIL import Image,  ImageOps
import customtkinter as ctk
import Globalne as glb


class Obraz(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Profil")
        self.geometry("420x740+700+20")

        self.Background_Frame = ctk.CTkFrame(self,
                                             fg_color=glb.color_background,
                                             border_color=glb.color_background,
                                             width=420, height=740)
        self.Background_Frame.place(relx=0, rely=0, anchor="nw")
        self.Mask = Image.open('mask.png').convert('L')
        Uzytkownik = Image.open('uzytkownik.png')


        self.Profile_Img = ctk.CTkImage(dark_image=pil.Image.open("uzytkownik.png"), size=(200, 200))
        self.Profile_Button = ctk.CTkButton(self.Background_Frame, image=self.Profile_Img, text="",
                                             width=200, height=200,
                                             fg_color=glb.color_background,
                                             command=self.My_Upload,
                                             hover_color=glb.color_background,
                                             corner_radius=100)
        self.Profile_Button.place(relx=0.5,rely=0.25, anchor="center")



    def My_Upload(self):
        pass











Obraz().mainloop()