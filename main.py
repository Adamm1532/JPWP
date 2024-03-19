import tkinter as tk
import customtkinter as ctk

window = tk.Tk()
window.geometry("400x400")
window.configure(bg="#505cc2")
label = tk.Label(text="Hello, Tkinter!",
                 fg="black",
                 bg="#34A2FE",
                 width=10,
                 height=5, font=("Arial", 20))
label.pack()
window.mainloop()

#root = ctk.CTk()
#root.geometry("400x400")
#button = ctk.CTkButton(root, text="Click me!")
#button.place(relx=0.5, rely=0.5, anchor="center")
#root.mainloop()