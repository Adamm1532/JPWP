import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Name reader")
        self.geometry("400x400")
        self.text = ctk.CTkLabel(self, text="Hello there!", font=("Arial", 20), text_color="#29999c")
        self.text.place(relx=0.5, rely=0.1, anchor="center")
        self.entry = ctk.CTkEntry(self, placeholder_text="Enter your name", width=300, height=20, placeholder_text_color="#3ed2d7")
        self.entry.place(relx=0.5, rely=0.3, anchor="center")
        self.button = ctk.CTkButton(self, text="Check name", fg_color="#3ed2d7", hover_color="#29999c", command=self.clicked, width=120, height=50, corner_radius=10)
        self.button.place(relx=0.5, rely=0.5, anchor="center")
    def clicked(self):
        p = self.entry.get()
        self.button.configure(text=p)
        if p == "Deez Nuts":
            self.label = ctk.CTkLabel(self, text="HA! GOT EEM!", font=("Arial", 10))
            self.label.place(relx=0.5, rely=0.7, anchor="center")
            self.label.after(2000, lambda: self.label.destroy())



if __name__ == "__main__":
    app = App()
    app.mainloop()