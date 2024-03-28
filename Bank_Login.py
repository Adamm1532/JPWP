import time
import customtkinter as ctk
import PIL as pil
from threading import Thread



class Bank_Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bank Login")
        self.geometry("420x740+700+20")
        self.color_yellow = "#E6D525"
        self.color_magenta = "#E62569"
        self.color_blue = "#25C0E6"
        self.color_backgroundLight = "#f4edde"
        self.color_backgroundDark = "#565656"

        self.Frame_x=0
        self.backgroundFrame = ctk.CTkFrame(self,
                                            fg_color=self.color_backgroundLight,
                                            border_color=self.color_backgroundLight,
                                            width=420, height=740)
        self.backgroundFrame.place(relx=self.Frame_x, rely=0, anchor="nw")

        self.magenta_size = 150
        self.Magenta_Circle_img = ctk.CTkImage(dark_image=pil.Image.open("Circle_magenta.png"), size=(self.magenta_size, self.magenta_size))
        self.Magenta_Cirlce_Label = ctk.CTkLabel(self.backgroundFrame, image=self.Magenta_Circle_img, text="")
        self.Magenta_Cirlce_Label.place(x=30, y=50, anchor="center")

        self.yellow_x = 350
        self.yellow_y = 200
        self.Yellow_Circle_img = ctk.CTkImage(dark_image=pil.Image.open("Circle_yellow.png"), size=(200, 200))
        self.Yellow_Cirlce_Label = ctk.CTkLabel(self.backgroundFrame, image=self.Yellow_Circle_img, text="")
        self.Yellow_Cirlce_Label.place(x=self.yellow_x, y=self.yellow_y, anchor="nw")

        self.blue_x = 300
        self.blue_y = 700
        self.Blue_Circle_img = ctk.CTkImage(dark_image=pil.Image.open("Circle_blue.png"), size=(300, 300))
        self.Blue_Cirlce_Label = ctk.CTkLabel(self.backgroundFrame, image=self.Blue_Circle_img, text="")
        self.Blue_Cirlce_Label.place(x=self.blue_x, y=self.blue_y, anchor="center")

        self.Bank_Logo = ctk.CTkLabel(self.backgroundFrame,
                                 height=110, width=110,
                                 fg_color=self.color_magenta,
                                 text="Py",
                                 font=("Arial Rounded MT Bold", 60),
                                 text_color="white",
                                 corner_radius=20)
        self.Bank_x = 0.5
        self.Bank_Logo.place(relx=self.Bank_x, rely=0.3, anchor="e")

        self.Bank_Text = ctk.CTkLabel(self.backgroundFrame,
                                      height=110, width=110,
                                      text="Bank",
                                      font=("Arial Rounded MT Bold", 50),
                                      text_color="black")
        self.Bank_Text.place(relx=self.Bank_x, rely=0.3, anchor="w")

        self.Mail_Text = ctk.CTkLabel(self.backgroundFrame,
                                     text="Podaj swól e-mail:",
                                     font=("Arial", 20),
                                     text_color=self.color_magenta)
        self.Mail_Text.place(relx=self.Bank_x+0.05, rely=0.48, anchor="se")

        self.Entry_Mail = ctk.CTkEntry(self.backgroundFrame,
                                       placeholder_text="np. cos@tam.pl",
                                       fg_color="white",
                                       width=300, height=30,
                                       placeholder_text_color="gray",
                                       text_color="black")
        self.Entry_Mail.place(relx=self.Bank_x, rely=0.5, anchor="center")

        self.Password_Text = ctk.CTkLabel(self.backgroundFrame,
                                      text="Wpisze swoje hasło:",
                                      font=("Arial", 20),
                                      text_color=self.color_magenta)
        self.Password_Text.place(relx=self.Bank_x+0.1, rely=0.58, anchor="se")

        self.Entry_Password = ctk.CTkEntry(self.backgroundFrame,
                                       placeholder_text="np. masło",
                                       fg_color="white",
                                       width=300, height=30,
                                       placeholder_text_color="gray",
                                       text_color="black",
                                       show="*")
        self.Entry_Password.place(relx=self.Bank_x, rely=0.6, anchor="center")

        self.Button_Login = ctk.CTkButton(self.backgroundFrame,
                                        text="Zaloguj",
                                        fg_color=self.color_magenta,
                                        hover_color=self.color_blue,
                                        width=120, height=50,
                                        corner_radius=10,
                                        command=self.clicked)
        self.Button_Login.place(relx=self.Bank_x, rely=0.7, anchor="center")

    def clicked(self):
        correct_mail = ["adam@madon.pl", "dorian@sraga.pl", "1"]
        correct_password = ["12345", "dorian", "1"]
        if self.Entry_Mail.get() in correct_mail and self.Entry_Password.get() in correct_password:
            print("Debug: Zalogowano")
            Thread(target=self.magenta_expand()).start()
            Thread(target=self.yellow_move()).start()
            Thread(target=self.blue_move()).start()
            Thread(target=self.moveEverythingElse).start()
            Thread(target=self.destruction).start()
        else:
            print("Debug: Błędne dane")
            self.Wrong_Label()

    def Wrong_Label(self):
        self.Wrong = ctk.CTkLabel(self.backgroundFrame,
                                        text="Błędny e-mail i/lub hasło",
                                        font=("Arial", 20),
                                        text_color="red")
        self.Wrong.place(relx=0.5, rely=0.65, anchor="center")
        self.Wrong.after(1500, self.Wrong.destroy)

    def magenta_expand(self):
        try:
            if self.magenta_size <= 200:
                self.Magenta_Cirlce_Label.destroy()
                self.magenta_size += 10
                self.Magenta_Circle_img = ctk.CTkImage(dark_image=pil.Image.open("Circle_magenta.png"),
                                                       size=(self.magenta_size, self.magenta_size))
                self.Magenta_Cirlce_Label = ctk.CTkLabel(self.backgroundFrame, image=self.Magenta_Circle_img, text="")
                self.Magenta_Cirlce_Label.place(x=30, y=50, anchor="center")
                self.after(25, self.magenta_expand)
            else:
                self.magenta_reducing()
        except:
            pass
    def magenta_reducing(self):
        try:
            if self.magenta_size >= 10:
                self.Magenta_Cirlce_Label.destroy()
                self.magenta_size -= 10
                self.Magenta_Circle_img = ctk.CTkImage(dark_image=pil.Image.open("Circle_magenta.png"),
                                                       size=(self.magenta_size, self.magenta_size))
                self.Magenta_Cirlce_Label = ctk.CTkLabel(self.backgroundFrame, image=self.Magenta_Circle_img, text="")
                self.Magenta_Cirlce_Label.place(x=30, y=50, anchor="center")
                self.after(25, self.magenta_reducing)
        except:
            pass

    def yellow_move(self):
        if self.yellow_x <= 450:
            self.yellow_x += 5
            self.Yellow_Cirlce_Label.place(x=self.yellow_x, y=self.yellow_y, anchor="nw")
            self.after(25, self.yellow_move)

    def blue_move(self):
        if self.blue_y <= 1000:
            self.blue_y += 10
            self.Blue_Cirlce_Label.place(x=self.blue_x, y=self.blue_y, anchor="center")
            self.after(25, self.blue_move)

    def moveEverythingElse(self):
        if self.Bank_x<4:
            self.Bank_x += 0.05
            self.Bank_Logo.place(relx=self.Bank_x, rely=0.3, anchor="e")
            self.Bank_Text.place(relx=self.Bank_x, rely=0.3, anchor="w")
            self.Mail_Text.place(relx=self.Bank_x+0.05, rely=0.48, anchor="se")
            self.Entry_Mail.place(relx=self.Bank_x, rely=0.5, anchor="center")
            self.Password_Text.place(relx=self.Bank_x+0.1, rely=0.58, anchor="se")
            self.Entry_Password.place(relx=self.Bank_x, rely=0.6, anchor="center")
            self.Button_Login.place(relx=self.Bank_x, rely=0.7, anchor="center")
            self.after(25, self.moveEverythingElse)
        # self.Frame_x += 0.1
        # self.backgroundFrame.place(relx=self.Frame_x, rely=0, anchor="nw")
        # self.after(20, self.moveEverythingElse)

    def destruction(self):
        self.after(2000, self.destroy)
        time.sleep(2)
        import Bank_Ustawienia


if __name__ == "__main__":
    app = Bank_Login()
    app.mainloop()