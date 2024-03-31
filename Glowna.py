import time
from threading import Thread
import PIL as pil
import customtkinter as ctk
import Globalne as glb
from datetime import datetime
#import Bank_Ustawienia as Ust


class Glowna(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.ostatni_click = "nic"
        self.Settings_size = 30
        self.Settings_y = 0.05
        self.Settings_x = 0.9
        self.controller = controller

        self.background_frame = ctk.CTkFrame(self,
                                             fg_color=glb.color_background,
                                             border_color=glb.color_background,
                                             width=420, height=740)
        self.background_frame.place(relx=0, rely=0, anchor="nw")

        self.Saldo_Label = ctk.CTkLabel(self.background_frame,
                                        height=30, width=80,
                                        corner_radius=10,
                                        text="Stan Konta: " + str(glb.Saldo) + " zł",
                                        font=("Arial", 20, "bold"),
                                        text_color=glb.color_text, fg_color=glb.color_background)
        self.Saldo_Label.place(relx=0.5, rely=0.22, anchor="center")

        # self.my_frame = Historia(master=self, width=300, height=200,fg_color= "transparent")
        # self.my_frame.place(relx=0.1, rely=0.7, anchor="w")
        self.historia_scrol = ctk.CTkScrollableFrame(master=self,
                                                     bg_color=glb.color_background,
                                                     border_color=glb.color_magenta,
                                                     border_width=0,
                                                     width=300,
                                                     height=400,
                                                     fg_color=glb.color_background2,
                                                     label_text="Historia tranzakcji",
                                                     label_font=("Arial", 20, "bold"),
                                                     label_fg_color=glb.color_yellow,
                                                     scrollbar_button_color=glb.color_magenta,
                                                     corner_radius=10, )
        self.historia_scrol.place(relx=0.5, rely=0.6, anchor="center")

        self.buttons = []  # List to store button instances
        self.labels = []

        self.rodzaj = []  # List to store button instances
        self.ilosc = []  # List to store label instances
        # getting the current date and time
        current_datetime = datetime.now()

        current_date_time = current_datetime.strftime("%H:%M:%S  %m/%d/%Y")

        for x in range(0, len(glb.historia1), 2):
            label = ctk.CTkLabel(self.historia_scrol, text=glb.historia1[x], fg_color=glb.color_background2, text_color=glb.color_text)
            label.grid(row=x, column=1, padx=(10, 81), pady=10, sticky=ctk.W, )
            self.rodzaj.append(label)

            label2 = ctk.CTkLabel(self.historia_scrol, text=str(glb.historia1[x + 1]) + " zł",
                                  fg_color=glb.color_background2, text_color=glb.color_text)
            label2.grid(row=x, column=2, padx=(10, 5), pady=10, sticky=ctk.W)
            self.ilosc.append(label2)

            self.arrow1_img = ctk.CTkImage(dark_image=glb.arrow1, size=(30, 30))
            self.arrow2_img = ctk.CTkImage(dark_image=glb.arrow2, size=(30, 30))
            arrow_button = ctk.CTkButton(self.historia_scrol, image=self.arrow1_img, text="",
                                         width=20, height=20,
                                         fg_color=glb.color_background2,
                                         command=lambda x=x: self.expand(x),
                                         hover_color=glb.color_background2)
            arrow_button.grid(row=x, column=0, padx=(10, 5), pady=10, sticky=ctk.W)
            self.buttons.append(arrow_button)

            label_czas = ctk.CTkLabel(self.historia_scrol, text=current_date_time, fg_color=glb.color_background2,
                                      text_color=glb.color_background2, width=0, height=0)
            # label_czas.grid(row=x+1, column=1, padx=(10, 5), pady=10, sticky=ctk.W,)
            self.labels.append(label_czas)

        self.Settings_img = ctk.CTkImage(dark_image=glb.settings_button, size=(self.Settings_size, self.Settings_size))
        self.Settings_Button = ctk.CTkButton(self.background_frame, image=self.Settings_img, text="",
                                             width=50, height=50,
                                             fg_color=glb.color_background,
                                             command=self.Settings_open,
                                             hover_color=glb.color_background)
        self.Settings_Button.place(relx=self.Settings_x, rely=self.Settings_y, anchor="center")
        self.Profile_img = ctk.CTkImage(dark_image=glb.Profile_button, size=(30, 30))
        self.Profile_Button = ctk.CTkButton(self.background_frame, image=self.Profile_img, text="",
                                            width=50, height=50,
                                            fg_color=glb.color_background,
                                            hover_color=glb.color_background,
                                            command=self.Profil_open)
        self.Profile_Button.place(relx=0.1, rely=self.Settings_y, anchor="center")

    def expand(self, x):
        for button in self.buttons:
            button.configure(image=self.arrow1_img)
        for label in self.labels:
            label.configure(text_color=glb.color_background2, width=0, height=0)
            label.grid_remove()

        # Change the image in the clicked button
        if self.ostatni_click != x:
            self.buttons[x // 2].configure(image=self.arrow2_img)
            self.labels[x // 2].configure(text_color=glb.color_blue, width=2, height=2)
            self.labels[x // 2].grid(row=x + 1, column=1, padx=(10, 5), pady=10, sticky=ctk.W, )
            self.ostatni_click = x
        else:
            self.ostatni_click = "nic"

    def zwieksz_settings(self):
        while self.Settings_size <= 50:
            self.Settings_size *= 1.1

            self.Settings_img = ctk.CTkImage(dark_image=glb.settings_button,
                                             size=(self.Settings_size, self.Settings_size))
            self.Settings_Button.configure(image=self.Settings_img)
            self.update_idletasks()  # Aktualizuj interfejs użytkownika
            time.sleep(0.001)

    def Settings_open(self):
        self.controller.show_frame("Ustawienia")

    def Profil_open(self):
        self.controller.show_frame("Profil")

    def change_mode_dark(self):
        self.background_frame.configure(fg_color=glb.color_background, border_color=glb.color_background)
        self.Saldo_Label.configure(fg_color=glb.color_background, text_color=glb.color_text)
        self.Settings_Button.configure(fg_color=glb.color_background, hover_color=glb.color_background)
        self.Profile_Button.configure(fg_color=glb.color_background, hover_color=glb.color_background)
        self.historia_scrol.configure(bg_color=glb.color_background, fg_color=glb.color_background2)
        for button in self.buttons:
            button.configure(fg_color=glb.color_background2, hover_color=glb.color_background2)
        for label in self.labels:
            label.configure(fg_color=glb.color_background2)
        for label in self.rodzaj:
            label.configure(fg_color=glb.color_background2, text_color=glb.color_text)
        for label in self.ilosc:
            label.configure(fg_color=glb.color_background2, text_color=glb.color_text)

    def change_mode_light(self):
        self.background_frame.configure(fg_color=glb.color_background, border_color=glb.color_background)
        self.Saldo_Label.configure(fg_color=glb.color_background, text_color=glb.color_text)
        self.Settings_Button.configure(fg_color=glb.color_background, hover_color=glb.color_background)
        self.Profile_Button.configure(fg_color=glb.color_background, hover_color=glb.color_background)
        self.historia_scrol.configure(bg_color=glb.color_background, fg_color=glb.color_background2)
        for button in self.buttons:
            button.configure(fg_color=glb.color_background2, hover_color=glb.color_background2)
        for label in self.labels:
            label.configure(fg_color=glb.color_background2)
        for label in self.rodzaj:
            label.configure(fg_color=glb.color_background2, text_color=glb.color_text)
        for label in self.ilosc:
            label.configure(fg_color=glb.color_background2, text_color=glb.color_text)