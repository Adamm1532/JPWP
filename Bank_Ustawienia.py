import customtkinter as ctk

class Ustawienia(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ustawienia")
        self.geometry("420x740+700+20")
        self.color_yellow = "#E6D525"
        self.color_magenta = "#E62569"
        self.color_blue = "#25C0E6"
        self.color_backgroundLight = "#f4edde"
        self.color_backgroundDark = "#565656"
        self.background_frame = ctk.CTkFrame(self,
                                             fg_color=self.color_backgroundLight,
                                             border_color=self.color_backgroundLight,
                                             width=420, height=740)
        self.background_frame.place(relx=0, rely=0, anchor="nw")

        self.Setting_Label = ctk.CTkLabel(self.background_frame,
                                          height=60, width=110,
                                          padx=10, pady=10,
                                          corner_radius=10,
                                          text="Ustawienia",
                                          font=("Arial", 30, "bold"),
                                          text_color="white",
                                          fg_color=self.color_magenta)
        self.Setting_Label.place(relx=0.07, rely=0.1, anchor="w")

        self.Limity_Label = ctk.CTkLabel(self.background_frame,
                                         height=30, width=80,
                                         corner_radius=10,
                                         text="Limity",
                                         font=("Arial", 20, "bold"),
                                         text_color="white", fg_color=self.color_magenta)
        self.Limity_Label.place(relx=0.1, rely=0.2, anchor="w")

        self.Limity_przelewy_Label = ctk.CTkLabel(self.background_frame,
                                                  height=20, width=110,
                                                  text="Limit przelewów: ",
                                                  font=("Arial", 15, "bold"),
                                                  text_color="black")
        self.Limity_przelewy_Label.place(relx=0.1, rely=0.25, anchor="w")
        self.przelew_liczba = 500
        self.Limity_przelewy_liczba = ctk.CTkLabel(self.background_frame,
                                                  height=10, width=10,
                                                  text=self.przelew_liczba,
                                                  font=("Arial", 15, "bold"),
                                                  text_color="black")
        self.Limity_przelewy_liczba.place(relx=0.48, rely=0.2511, anchor="w")
        self.Limity_przelewy_slider = ctk.CTkSlider(self.background_frame, from_=0, to=1000, width=300,
                                                    border_width=5, progress_color=self.color_yellow, button_color=self.color_yellow,
                                                    button_hover_color= self.color_magenta,
                                                    command=self.update_liczba_przelewy,
                                                    hover=False)
        self.Limity_przelewy_slider.place(relx=0.5, rely=0.3, anchor="center")

        self.Limity_karty_Label = ctk.CTkLabel(self.background_frame,
                                                  height=20, width=110,
                                                  text="Limit karty: ",
                                                  font=("Arial", 15, "bold"),
                                                  text_color="black")
        self.Limity_karty_Label.place(relx=0.075, rely=0.35, anchor="w")
        self.karty_liczba = 500
        self.Limity_karty_liczba = ctk.CTkLabel(self.background_frame,
                                                   height=10, width=10,
                                                   text=self.karty_liczba,
                                                   font=("Arial", 15, "bold"),
                                                   text_color="black")
        self.Limity_karty_liczba.place(relx=0.48, rely=0.3501, anchor="w")
        self.Limity_karty_slider = ctk.CTkSlider(self.background_frame, from_=0, to=1000, width=300,
                                                    border_width=5, progress_color=self.color_yellow,
                                                    button_color=self.color_yellow,
                                                    button_hover_color=self.color_magenta,
                                                    command=self.update_liczba_karty,
                                                    hover=False)
        self.Limity_karty_slider.place(relx=0.5, rely=0.4, anchor="center")

        self.Limity_Label = ctk.CTkLabel(self.background_frame,
                                         height=30, width=80,
                                         corner_radius=10,
                                         text="Limity",
                                         font=("Arial", 20, "bold"),
                                         text_color="white", fg_color=self.color_magenta)
        self.Limity_Label.place(relx=0.1, rely=0.2, anchor="w")


    def update_liczba_przelewy(self, value):
        value = round(value, 2)
        self.Limity_przelewy_liczba.configure(text=value)
        self.przelew_liczba = value

    def update_liczba_karty(self, value):
        value = round(value, 2)
        self.Limity_karty_liczba.configure(text=value)
        self.karty_liczba = value

Ustawienia().mainloop()