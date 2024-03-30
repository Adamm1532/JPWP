import customtkinter as ctk
import Globalne as glb
import PIL as pil
import Glowna as gl

class Ustawienia(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.background_frame = ctk.CTkFrame(self,
                                             fg_color=glb.color_background,
                                             border_color=glb.color_background,
                                             width=420, height=740)
        self.background_frame.place(relx=0, rely=0, anchor="nw")

        self.Back_img = ctk.CTkImage(dark_image=glb.back_button, size=(30, 30))
        self.Back_Button = ctk.CTkButton(self.background_frame, image=self.Back_img, text="",
                                         width=50, height=50,
                                         fg_color=glb.color_background,
                                         command=self.Back,
                                         hover_color=glb.color_background)
        self.Back_Button.place(relx=0.07, rely=0.05, anchor="center")

        self.Setting_Label = ctk.CTkLabel(self.background_frame,
                                          height=60, width=110,
                                          padx=10, pady=10,
                                          corner_radius=10,
                                          text="Ustawienia",
                                          font=("Arial", 30, "bold"),
                                          text_color="white",
                                          fg_color=glb.color_magenta)
        self.Setting_Label.place(relx=0.65, rely=0.1, anchor="center")

        self.Limity_Label = ctk.CTkLabel(self.background_frame,
                                         height=30, width=80,
                                         corner_radius=10,
                                         text="Limity",
                                         font=("Arial", 20, "bold"),
                                         text_color="white", fg_color=glb.color_magenta)
        self.Limity_Label.place(relx=0.1, rely=0.22, anchor="w")

        self.Limity_przelewy_Label = ctk.CTkLabel(self.background_frame,
                                                  height=20, width=110,
                                                  text="Limit przelewów: ",
                                                  font=("Arial", 15, "bold"),
                                                  text_color=glb.color_text)
        self.Limity_przelewy_Label.place(relx=0.1, rely=0.27, anchor="w")
        self.Limity_przelewy_liczba = ctk.CTkLabel(self.background_frame,
                                                  height=10, width=10,
                                                  text=glb.przelew_liczba,
                                                  font=("Arial", 15, "bold"),
                                                  text_color=glb.color_text)
        self.Limity_przelewy_liczba.place(relx=0.48, rely=0.2701, anchor="w")
        self.Limity_przelewy_slider = ctk.CTkSlider(self.background_frame, from_=0, to=1000, width=300,
                                                    border_width=5, progress_color=glb.color_yellow,
                                                    button_color=glb.color_yellow,
                                                    button_hover_color= glb.color_magenta,
                                                    command=self.update_liczba_przelewy,
                                                    hover=False)
        self.Limity_przelewy_slider.place(relx=0.5, rely=0.32, anchor="center")

        self.Limity_karty_Label = ctk.CTkLabel(self.background_frame,
                                                  height=20, width=110,
                                                  text="Limit karty: ",
                                                  font=("Arial", 15, "bold"),
                                                  text_color=glb.color_text)
        self.Limity_karty_Label.place(relx=0.075, rely=0.37, anchor="w")
        self.Limity_karty_liczba = ctk.CTkLabel(self.background_frame,
                                                   height=10, width=10,
                                                   text=glb.karta_liczba,
                                                   font=("Arial", 15, "bold"),
                                                   text_color=glb.color_text)
        self.Limity_karty_liczba.place(relx=0.48, rely=0.3701, anchor="w")
        self.Limity_karty_slider = ctk.CTkSlider(self.background_frame, from_=0, to=1000, width=300,
                                                    border_width=5, progress_color=glb.color_yellow,
                                                    button_color=glb.color_yellow,
                                                    button_hover_color=glb.color_magenta,
                                                    command=self.update_liczba_karty,
                                                    hover=False)
        self.Limity_karty_slider.place(relx=0.5, rely=0.42, anchor="center")

        self.System_Label = ctk.CTkLabel(self.background_frame,
                                         height=30, width=80,
                                         corner_radius=10,
                                         text="System",
                                         font=("Arial", 20, "bold"),
                                         text_color="white", fg_color=glb.color_magenta)
        self.System_Label.place(relx=0.1, rely=0.5, anchor="w")

        self.Mobile_Label = ctk.CTkLabel(self.background_frame,
                                         height=20, width=110,
                                         text="Przelewy mobline: ",
                                         font=("Arial", 15, "bold"),
                                         text_color=glb.color_text)
        self.Mobile_Label.place(relx=0.1, rely=0.56, anchor="w")
        self.Mobile_Switch = ctk.CTkSwitch(self.background_frame,
                                           switch_width=45, switch_height=25,
                                           fg_color=glb.color_magenta,
                                           button_color=glb.color_yellow,
                                           hover=False,
                                           progress_color=glb.color_blue,
                                           text="")
        self.Mobile_Switch.place(relx=0.84, rely=0.56, anchor="center")

        self.Notification_Label = ctk.CTkLabel(self.background_frame,
                                         height=20, width=110,
                                         text="Powiadomienia: ",
                                         font=("Arial", 15, "bold"),
                                         text_color=glb.color_text)
        self.Notification_Label.place(relx=0.1, rely=0.63, anchor="w")
        self.Notification_Switch = ctk.CTkSwitch(self.background_frame,
                                           switch_width=45, switch_height=25,
                                           fg_color=glb.color_magenta,
                                           button_color=glb.color_yellow,
                                           hover=False,
                                           progress_color=glb.color_blue,
                                           text="")
        self.Notification_Switch.place(relx=0.84, rely=0.63, anchor="center")

        self.Warning_Label = ctk.CTkLabel(self.background_frame,
                                               height=20, width=110,
                                               text="Ostrzeżenie przed przelewem: ",
                                               font=("Arial", 15, "bold"),
                                               text_color=glb.color_text)
        self.Warning_Label.place(relx=0.1, rely=0.7, anchor="w")
        self.Warning_Switch = ctk.CTkSwitch(self.background_frame,
                                                 switch_width=45, switch_height=25,
                                                 fg_color=glb.color_magenta,
                                                 button_color=glb.color_yellow,
                                                 hover=False,
                                                 progress_color=glb.color_blue,
                                                 text="")
        self.Warning_Switch.place(relx=0.84, rely=0.7, anchor="center")

        self.DarkMode_Label = ctk.CTkLabel(self.background_frame,
                                          height=20, width=110,
                                          text="Light Mode / Dark Mode: ",
                                          font=("Arial", 15, "bold"),
                                          text_color=glb.color_text)
        self.DarkMode_Label.place(relx=0.1, rely=0.77, anchor="w")
        self.DarkMode_Switch = ctk.CTkSwitch(self.background_frame,
                                            switch_width=45, switch_height=25,
                                            fg_color=glb.color_magenta,
                                            button_color=glb.color_yellow,
                                            hover=False,
                                            progress_color=glb.color_blue,
                                            command=self.change_mode,
                                            onvalue=1,
                                            offvalue=0,
                                            text="")
        self.DarkMode_Switch.place(relx=0.84, rely=0.77, anchor="center")

        self.LogOut_Button = ctk.CTkButton(self.background_frame,
                                         text="Wyloguj",
                                         fg_color=glb.color_magenta,
                                         hover_color=glb.color_blue,
                                         width=80, height=30,
                                         corner_radius=10,
                                         command=self.Back_Login)
        self.LogOut_Button.place(relx=0.5, rely=0.9, anchor="center")

    def update_liczba_przelewy(self, value):
        value = round(value, 2)
        self.Limity_przelewy_liczba.configure(text=value)
        glb.przelew_liczba = value

    def update_liczba_karty(self, value):
        value = round(value, 2)
        self.Limity_karty_liczba.configure(text=value)
        glb.karty_liczba = value

    def Back(self):
        self.controller.show_frame("Glowna")

    def Back_Login(self):
        self.controller.show_frame("Bank_Login")


    def change_mode(self):
        if self.DarkMode_Switch.get() == 1:
            glb.color_text = "white"
            glb.color_background = "#414141"
            glb.color_background2 = "#023534"
            glb.back_button = pil.Image.open("back_darkmode.png")
            self.background_frame.configure(fg_color=glb.color_background,
                                            border_color=glb.color_background)
            self.Back_img = ctk.CTkImage(dark_image=glb.back_button, size=(30, 30))
            self.Back_Button.configure(fg_color=glb.color_background,
                                      hover_color=glb.color_background,
                                       image=self.Back_img)
            self.Limity_przelewy_Label.configure(text_color=glb.color_text)
            self.Limity_przelewy_liczba.configure(text_color=glb.color_text)
            self.Limity_karty_Label.configure(text_color=glb.color_text)
            self.Limity_karty_liczba.configure(text_color=glb.color_text)
            self.Mobile_Label.configure(text_color=glb.color_text)
            self.Notification_Label.configure(text_color=glb.color_text)
            self.Warning_Label.configure(text_color=glb.color_text)
            self.DarkMode_Label.configure(text_color=glb.color_text)
            self.controller.change_mode_dark("Glowna")
            self.controller.change_mode_dark("Bank_Login")
        else:
            glb.color_text = "black"
            glb.color_background = "#F4EDDE"
            glb.color_background2 = "#e5d4b1"
            glb.back_button = pil.Image.open("back.png")
            self.background_frame.configure(fg_color=glb.color_background,
                                            border_color=glb.color_background)
            self.Back_img = ctk.CTkImage(dark_image=glb.back_button, size=(30, 30))
            self.Back_Button.configure(fg_color=glb.color_background,
                                      hover_color=glb.color_background,
                                       image=self.Back_img)
            self.Limity_przelewy_Label.configure(text_color=glb.color_text)
            self.Limity_przelewy_liczba.configure(text_color=glb.color_text)
            self.Limity_karty_Label.configure(text_color=glb.color_text)
            self.Limity_karty_liczba.configure(text_color=glb.color_text)
            self.Mobile_Label.configure(text_color=glb.color_text)
            self.Notification_Label.configure(text_color=glb.color_text)
            self.Warning_Label.configure(text_color=glb.color_text)
            self.DarkMode_Label.configure(text_color=glb.color_text)
            self.controller.change_mode_light("Glowna")
            self.controller.change_mode_light("Bank_Login")