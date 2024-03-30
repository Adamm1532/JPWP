import time
from threading import Thread
import PIL as pil
import customtkinter as ctk
import Globalne as glb
from datetime import datetime
#import Bank_Ustawienia as Ust
class Historia(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        
        label = ctk.CTkLabel(self, text= glb.historia1[0])
        label.grid(row=0, column=0, padx=(10, 5), pady=10, sticky=ctk.W)
        label2 = ctk.CTkLabel(self, text= glb.historia1[1])
        label2.grid(row=0, column=1, padx=(10, 5), pady=10, sticky=ctk.W)
        self.arrow1_img = ctk.CTkImage(dark_image=glb.arrow1, size=(30, 30))
        self.arrow1_Button = ctk.CTkButton(self, image=self.arrow1_img, text="",
                                         width=20, height=20,
                                         fg_color="transparent",
                                         
                                         #command=self.destruction,
                                         hover_color=glb.color_background)
        self.arrow1_Button.grid(row=0, column=2, padx=(10, 5), pady=10, sticky=ctk.W)




class Glowna(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Bank Login")
        self.geometry("420x740+700+20")
        self.ostatni_click = "nic"
        self.color_yellow = "#E6D525"
        self.color_magenta = "#E62569"
        self.color_blue = "#25C0E6"
        self.color_backgroundLight = "#f4edde"
        self.color_backgroundDark = "#565656"
        self.background_frame = ctk.CTkFrame(self,
                                             fg_color=glb.color_background,
                                             border_color=glb.color_background,
                                             width=420, height=740)
        self.background_frame.place(relx=0, rely=0, anchor="nw")

        self.Settings_img = ctk.CTkImage(dark_image=glb.settings_button, size=(30, 30))
        self.Settings_Button = ctk.CTkButton(self.background_frame, image=self.Settings_img, text="",
                                         width=50, height=500,
                                         fg_color=glb.color_background,
                                         
                                         command=self.destruction,
                                         hover_color=glb.color_background)
        self.Settings_Button.place(relx=0.9, rely=0.05, anchor="center")


        self.Saldo_Label = ctk.CTkLabel(self.background_frame,
                                         height=30, width=80,
                                         corner_radius=10,
                                         text="Stan Konta: " + str(glb.Saldo) + " zł",
                                         font=("Arial", 20, "bold"),
                                         text_color=glb.color_text, fg_color=glb.color_background)
        self.Saldo_Label.place(relx=0.5, rely=0.22, anchor="center")


        #self.my_frame = Historia(master=self, width=300, height=200,fg_color= "transparent")
        #self.my_frame.place(relx=0.1, rely=0.7, anchor="w")
        self.historia_scrol=ctk.CTkScrollableFrame(master=self, 
                                                   bg_color=glb.color_background,
                                                   border_color=glb.color_magenta,
                                                   border_width=0,width=300,
                                                   height=200,
                                                   fg_color= glb.color_background2,
                                                   label_text="Historia tranzakcji",
                                                   label_fg_color=glb.color_yellow,
                                                   scrollbar_button_color=glb.color_magenta,
                                                   corner_radius=10,)
        self.historia_scrol.place(relx=0.5, rely=0.7, anchor="center")


        self.buttons = []  # List to store button instances
        self.labels = []   # List to store label instances
        # getting the current date and time
        current_datetime = datetime.now()


        current_date_time = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
        



        for x in range(0,len(glb.historia1),2):
            
            label = ctk.CTkLabel(self.historia_scrol, text= glb.historia1[x], fg_color=glb.color_background2)
            label.grid(row=x, column=1, padx=(10, 81), pady=10, sticky=ctk.W,)


            label2 = ctk.CTkLabel(self.historia_scrol, text= glb.historia1[x+1],fg_color=glb.color_background2)
            label2.grid(row=x, column=2, padx=(10, 5), pady=10, sticky=ctk.W)
            self.arrow1_img = ctk.CTkImage(dark_image=glb.arrow1, size=(30, 30))
            self.arrow2_img = ctk.CTkImage(dark_image=glb.arrow2, size=(30, 30))
            arrow_button = ctk.CTkButton(self.historia_scrol, image=self.arrow1_img, text="",
                                        width=20, height=20,
                                        fg_color=glb.color_background2,
                                        command=lambda x=x: self.expand(x),
                                        hover_color=glb.color_background2)
            arrow_button.grid(row=x, column=0, padx=(10, 5), pady=10, sticky=ctk.W)
            self.buttons.append(arrow_button)
            
            label_czas = ctk.CTkLabel(self.historia_scrol, text= current_date_time, fg_color=glb.color_background2,text_color=glb.color_background2,width=0, height=0)
            #label_czas.grid(row=x+1, column=1, padx=(10, 5), pady=10, sticky=ctk.W,)
            self.labels.append(label_czas)
            
    #def is_grid_cell_empty(self,frame, row, column):
    # Get grid information of the frame
        #grid_info = frame.grid_info()

         #   # Check if the given row and column exists in the grid
        #if f'row{row}' not in grid_info or f'column{column}' not in grid_info:
         #       return True  # Cell is empty
       # else:
                # Check if there are any widgets in the given row and column
       #     widgets = frame.grid_slaves(row=row, column=column)
       #     print ("Debug", len(widgets) )
       #     if len(widgets) == 0 : # If no widgets, cell is empty
       #         return True
       #     else:
       #         return False

    def expand(self,x):
        

        for button in self.buttons:
            button.configure(image=self.arrow1_img)
        for label in self.labels:
            label.configure(text_color=glb.color_background2,width=0, height=0)
            label.grid_remove()

    # Change the image in the clicked button
        print("Debug: " ,self.ostatni_click)    
        if self.ostatni_click != x:
        
            self.buttons[x//2].configure(image=self.arrow2_img)
            self.labels[x//2].configure(text_color=glb.color_blue,width=2, height=2)
            self.labels[x//2].grid(row=x+1, column=1, padx=(10, 5), pady=10, sticky=ctk.W,)
            self.ostatni_click = x
        else:
            self.ostatni_click = "nic"



    def destruction(self):
        self.destroy()
        
    def Settings_open(self):
        self.destroy
        


Glowna().mainloop()
#import Bank_Ustawienia