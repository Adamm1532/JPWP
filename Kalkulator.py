import customtkinter as ctk

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kalkulator")
        self.evwidth = 400
        self.bwidth1 = self.evwidth/4 - 20
        self.configure(bg_color="#181b1f")  # background color of app
        self.obc = "#fb2f64"  # color of +,-,*,/
        self.obch = "#cc2753"  # hover color of +,-,*,/
        self.nbc = "#181b1f"  # color of 0-9 same as the window's background
        self.nbch = "#14161a" #hover color of 0-9
        self.entry = ctk.CTkEntry(self, width=self.evwidth, placeholder_text="0")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.button1 = ctk.CTkButton(self, text="1", command=lambda: self.g_num("1"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button1.grid(row=3, column=0, padx=5, pady=10)
        self.button2 = ctk.CTkButton(self, text="2", command=lambda: self.g_num("2"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button2.grid(row=3, column=1, padx=5, pady=10)
        self.button3 = ctk.CTkButton(self, text="3", command=lambda: self.g_num("3"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button3.grid(row=3, column=2, padx=5, pady=10)
        self.button4 = ctk.CTkButton(self, text="4", command=lambda: self.g_num("4"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button4.grid(row=2, column=0, padx=5, pady=10)
        self.button5 = ctk.CTkButton(self, text="5", command=lambda: self.g_num("5"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button5.grid(row=2, column=1, padx=5, pady=10)
        self.button6 = ctk.CTkButton(self, text="6", command=lambda: self.g_num("6"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button6.grid(row=2, column=2, padx=5, pady=10)
        self.button7 = ctk.CTkButton(self, text="7", command=lambda: self.g_num("7"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button7.grid(row=1, column=0, padx=5, pady=10)
        self.button8 = ctk.CTkButton(self, text="8", command=lambda: self.g_num("8"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button8.grid(row=1, column=1, padx=5, pady=10)
        self.button9 = ctk.CTkButton(self, text="9", command=lambda: self.g_num("9"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button9.grid(row=1, column=2, padx=5, pady=10)
        self.button0 = ctk.CTkButton(self, text="0", command=lambda: self.g_num("0"),  fg_color=self.nbc, hover_color=self.nbch, width=self.bwidth1)
        self.button0.grid(row=4, column=0, padx=5, pady=10)
        self.button_plus = ctk.CTkButton(self, text="+", command=lambda: self.operate("+"), fg_color=self.obc, hover_color=self.obch, width=self.bwidth1)
        self.button_plus.grid(row=1, column=3, padx=5, pady=10)
        self.button_minus = ctk.CTkButton(self, text="-", command=lambda: self.operate("-"), fg_color=self.obc, hover_color=self.obch, width=self.bwidth1)
        self.button_minus.grid(row=2, column=3, padx=5, pady=10)
        self.button_multiply = ctk.CTkButton(self, text="*", command=lambda: self.operate("*"), fg_color=self.obc, hover_color=self.obch, width=self.bwidth1)
        self.button_multiply.grid(row=3, column=3, padx=5, pady=10)
        self.button_divide = ctk.CTkButton(self, text="/", command=lambda: self.operate("/"), fg_color=self.obc, hover_color=self.obch, width=self.bwidth1)
        self.button_divide.grid(row=4, column=3, padx=5, pady=10)
        self.button_equal = ctk.CTkButton(self, text="=", command=self.evaluate, width=self.bwidth1)
        self.button_equal.grid(row=4, column=2, padx=5, pady=10)
        self.button_clear = ctk.CTkButton(self, text="C", command=self.all_clear, width=self.bwidth1)
        self.button_clear.grid(row=4, column=1, padx=5, pady=10)

    def g_num(self, n):
        new_num = self.entry.get() + n
        self.entry.delete(0, "end")
        self.entry.insert(0, new_num)
    def all_clear(self):
        self.entry.delete(0, "end")

    def operate(self, op):
        self.first_num = int(self.entry.get())
        self.entry.delete(0, "end")
        self.operation = op

    def evaluate(self):
        second_num = int(self.entry.get())
        self.entry.delete(0, "end")
        if self.operation == "+":
            self.entry.insert(0, self.first_num + second_num)
        elif self.operation == "-":
            self.entry.insert(0, self.first_num - second_num)
        elif self.operation == "*":
            self.entry.insert(0, self.first_num * second_num)
        elif self.operation == "/":
            self.entry.insert(0, self.first_num / second_num)



if __name__ == "__main__":
    app = Calculator()
    app.mainloop()