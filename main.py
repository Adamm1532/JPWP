import tkinter as tk
import customtkinter as ctk

# def get_text():
#     text = entry.get()
#     print(text)
#
# window = tk.Tk()
# window.geometry("400x400")
# window.configure(bg="#505cc2")
# label = tk.Label(text="Hello, Tkinter!",
#                  fg="black",
#                  bg="#34A2FE",
#                  width=10,
#                  height=5, font=("Arial", 20))
# label.pack()
# button = tk.Button(text="Click me!", width=10, height=5, bg="white", fg="black", command = get_text)
# button.pack()
# entry = tk.Entry(fg="black", bg="white", width=50)
# entry.pack()
# window.mainloop()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Button command
def clicked():
    p = entry.get()
    label = ctk.CTkLabel(root, text=f"Hello, {p}!", font=("Arial", 10))
    label.place(relx=0.5, rely=0.6, anchor="center")

#window
root = ctk.CTk()
root.title("Custom Tkinter")
root.geometry("400x400")

#Label
text = ctk.CTkLabel(root, text="Hello there!", font=("Arial", 20))
#text.grid(row=0, column=0, padx=10, pady=10)
text.pack()

#Label 2
text2 = ctk.CTkLabel(root, text="General Kenobi!", font=("Comic Sans MS", 20), text_color="#e74035")
#text2.grid(row=0, column=1, padx=10, pady=10)
text2.place(relx=0.5, rely=0.3, anchor="center")

#Entry widget
entry = ctk.CTkEntry(root, placeholder_text="Enter your name", width=300, height=20, placeholder_text_color="green")
entry.place(relx=0.5, rely=0.4, anchor="center")

#Button
button = ctk.CTkButton(root, text="Click me!", fg_color="#e74035", hover_color="#9621b2", command=clicked, width=120, height=50, corner_radius=10)
button.place(relx=0.5, rely=0.5, anchor="center")
#button.configure(state="disabled")

root.mainloop()