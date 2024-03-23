import customtkinter as ctk

class Form(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Form")
        self.geometry("400x400")
        self.color1 = "#29999c"
        self.color2 = "#3ed2d7"
        self.text = ctk.CTkLabel(self, text="Welcome to {Website}!", font=("Arial", 20), text_color=self.color1)
        self.text.place(relx=0.5, rely=0.1, anchor="center")
        self.mail = ctk.CTkEntry(self, placeholder_text="Enter your mail", width=300, height=20, placeholder_text_color=self.color2)
        self.mail.place(relx = 0, rely=0.3, anchor="w")
        self.password = ctk.CTkEntry(self, placeholder_text="Enter your password", width=300, height=20,
                                  placeholder_text_color=self.color2)
        self.password.place(rely=0.4, anchor="w")
        self.button = ctk.CTkButton(self, text="Submit", fg_color=self.color2, hover_color=self.color1, command=self.clicked, width=120, height=50, corner_radius=10)
        self.button.place(relx = 0.5, rely=0.6, anchor="c")
    def clicked(self):
        correct_mail = ["cos@tam.pl", "zucc@erberc.com", "Deez@Nutz.com"]
        correct_password = ["cos", "zucc", "deeznuts"]
        mail = self.mail.get()
        password = self.password.get()
        if mail == correct_mail[0] and password == correct_password[0]:
            self.text.configure(text="Welcome, Cos Tam!")
        elif mail == correct_mail[1] and password == correct_password[1]:
            self.text.configure(text="Welcome, Zucc Erberc!")
        elif mail == correct_mail[2] and password == correct_password[2]:
            self.text.configure(text="Welcome, Deez Nuts!")
        else:
            self.label = ctk.CTkLabel(self, text="Wrong password and/or email", font=("Arial", 10), text_color="red")
            self.label.place(relx=0.5, rely=0.7, anchor="center")
            self.label.after(1000, lambda: self.label.destroy())


if __name__ == "__main__":
    app = Form()
    app.mainloop()