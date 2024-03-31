import customtkinter as ctk
import Bank_Login as bl
import Bank_Ustawienia as bu
import Glowna as gl
import Profil as pr

class Launch(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)

        self.title_font = ctk.CTkFont(family='Helvetica', size=18, weight="bold", slant="italic")
        self.geometry("420x740+700+20")

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (bl.Bank_Login, bu.Ustawienia, gl.Glowna, pr.Profil):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Bank_Login")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def change_mode_dark(self, page_name):
        self.frames[page_name].change_mode_dark()

    def change_mode_light(self, page_name):
        self.frames[page_name].change_mode_light()


if __name__ == "__main__":
    app = Launch()
    app.mainloop()