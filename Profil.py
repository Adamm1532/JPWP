import time
from threading import Thread
import PIL as pil
from PIL import Image, ImageTk, ImageOps
import customtkinter as ctk
import Globalne as glb
from datetime import datetime
import os

class Profil(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Profil")
        self.geometry("420x740+700+20")

        self.background_frame = ctk.CTkFrame(self,
                                             fg_color=glb.color_background,
                                             border_color=glb.color_background,
                                             width=420, height=740)
        self.background_frame.place(relx=0, rely=0, anchor="nw")

        self.mask = Image.open('mask.png').convert('L')
        im = Image.open('uzytkownik.png')

        output = ImageOps.fit(im, self.mask.size, centering=(0.5, 0.5))
        output.putalpha(self.mask)

        output.save('uzytkownik.png')
        
        # Empty label
        self.Empty_Label = ctk.CTkLabel(self.background_frame,
                                         height=350, width=250,
                                         corner_radius=10,
                                         text="",
                                         font=("Arial", 20, "bold"),
                                         text_color=glb.color_text, 
                                         fg_color="transparent")
        self.Empty_Label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.Empty_Label2 = ctk.CTkLabel(self.background_frame,
                                         height=200, width=200,
                                         corner_radius=10,
                                         text="",
                                         font=("Arial", 20, "bold"),
                                         text_color=glb.color_text, 
                                         fg_color="transparent")
        self.Empty_Label2.grid(row=6, column=0, columnspan=2, sticky="nsew")

        # Profile picture


        self.Pen_img = ctk.CTkImage(dark_image=glb.Pen, size=(30, 30))
        self.entry_opened = False  # Flag to track if entry is already opened
        self.change_buttons = []  # List to store change buttons
        self.change_labels = []   # List to store change labels
        change_texts = ["Zmiana nazwiska", "Zmiana imienia", "Zmiana telefonu", "Zmiana adresu"]
        for idx, button_text in enumerate(change_texts, start=2):
            label_text = f"{['Nazwisko', 'Imię', 'Telefon', 'Adres'][idx-2]}: {glb.Dane[idx-2]}"
            label = ctk.CTkLabel(self.background_frame,
                                height=30, width=200,
                                corner_radius=10,
                                text=label_text,
                                font=("Arial", 20, "bold"),
                                text_color=glb.color_text, 
                                fg_color=glb.color_background,
                                anchor="w")
            label.grid(row=idx, column=0, sticky="w", padx=10, pady=10)
            self.change_labels.append(label)

            button = ctk.CTkButton(self.background_frame, image=self.Pen_img,
                                    width=200, height=30,
                                    fg_color=glb.color_background,
                                    hover_color=glb.color_background,
                                    command=lambda idx=idx, label=label: self.change_info(idx, label, button))
            button.grid(row=idx, column=1, sticky="nsew", padx=100, pady=10)
            self.change_buttons.append(button)


        self.profile_img = ctk.CTkImage(dark_image=pil.Image.open("uzytkownik.png"), size=(200, 200))
        self.Profile_Button = ctk.CTkButton(self.background_frame, image=self.profile_img, text="",
                                             width=200, height=200,
                                             fg_color=glb.color_background,
                                             command=self.my_upload,
                                             hover_color=glb.color_background,
                                             corner_radius=100)
        self.Profile_Button.place(relx=0.35,rely=0.25, anchor="center")

        # Back button
        self.Back_img = ctk.CTkImage(dark_image=glb.back_button, size=(30, 30))
        self.Back_Button = ctk.CTkButton(self.background_frame, image=self.Back_img, text="",
                                         width=50, height=50,
                                         fg_color=glb.color_background,
                                         hover_color=glb.color_background)
        self.Back_Button.place(relx=0.07, rely=0.05, anchor="center")

    def my_upload(self):
        global filename

        # User selects an image file
        f_types = [('All files', '*.*'), ('JPG', '*.jpg'), ('PNG', '*.png')]
        filename = ctk.filedialog.askopenfilename(filetypes=f_types)
        
        # Open the selected image file and assign it to the profile_img variable
        image_pil = Image.open(filename)
        output_filename = "uzytkownik.png"
        image_pil.save(output_filename, overwrite=True)  # Save PIL image
        im = Image.open('uzytkownik.png')

        output = ImageOps.fit(im, self.mask.size, centering=(0.5, 0.5))
        output.putalpha(self.mask)

        output.save('uzytkownik.png')
        self.profile_img = ctk.CTkImage(dark_image=Image.open("uzytkownik.png"), size=(200, 200))
        
        # Update the button image
        self.Profile_Button.configure(image=self.profile_img)


        
    def change_info(self, idx, label, button):
        if self.entry_opened:
            return  # Return if entry is already opened

        # Disable all change buttons
        for btn in self.change_buttons:
            btn.configure(state="disabled")
        
        self.entry_opened = True  # Set flag to True

        # Create a new entry widget
        new_entry = ctk.CTkEntry(self.background_frame, fg_color="white",
                                width=200, height=30,
                                placeholder_text=f"Enter new {['Nazwisko', 'Imię', 'Telefon', 'Adres'][idx-2]}")
        new_entry.grid(row=idx, column=0, sticky="w", padx=10, pady=10)

        # Function to update the label with the new information
        def update_label():
            new_info = new_entry.get()
            if new_info:
                glb.Dane[idx-2] = new_info  # Update global data
                label.configure(text=f"{['Nazwisko', 'Imię', 'Telefon', 'Adres'][idx-2]}: {new_info}")
                new_entry.destroy()  # Remove the entry widget after updating the label
                self.entry_opened = False  # Reset flag to False

                # Enable all change buttons
                for btn in self.change_buttons:
                    btn.configure(state="normal")
                # Disable the confirm button
            confirm_button.grid_remove()
        # Function to handle Enter key press
        def handle_enter(event):
            update_label()

        # Bind the Enter key press event to the entry widget
        new_entry.bind("<Return>", handle_enter)

        # Create a button to confirm the input
        confirm_button = ctk.CTkButton(self.background_frame, text="Potwierdź",
                                        text_color=glb.color_magenta,
                                        width=100, height=30,
                                        fg_color=glb.color_background,
                                        hover_color=glb.color_background,
                                        command=update_label)
        confirm_button.grid(row=idx, column=1, sticky="w", padx=10, pady=10)



Profil().mainloop()
