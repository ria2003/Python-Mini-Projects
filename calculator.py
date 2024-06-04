import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("360x520")
        self.title("Calculator")
        self.configure(bg="floral white")

        self.user_input=tk.Entry(self, font=("Arial", 20), bg="floral white", foreground="coral4", bd=0, justify="right")
        self.user_input.pack(fill=tk.BOTH, ipadx=30, ipady=10, padx=10, pady=(20,5))

        self.separator2 = tk.Frame(self, bd=10, relief='sunken', height=4)
        self.separator2.pack(fill='x', pady=(0,5))

        buttons_frame1=tk.Frame(self, bg="floral white")
        buttons_frame1.pack()

        self.btn1=tk.Button(buttons_frame1, text="AC", font=("Arial", 18), bg="LightPink4", fg="white", borderwidth=2, relief="flat", command=lambda t="AC": self.set_value(t))
        self.btn1.grid(row=0, column=0, padx=14, pady=14, ipadx=8, ipady=10)

        self.btn2=tk.Button(buttons_frame1, text="Del", font=("Arial", 18), bg="LightPink4", fg="white", borderwidth=2, relief="flat", command=lambda t="Del": self.set_value(t))
        self.btn2.grid(row=0, column=1, padx=(0,14), pady=14, ipadx=6, ipady=10)

        self.btn3=tk.Button(buttons_frame1, text="%", font=("Arial", 18), bg="LightPink4", fg="white", borderwidth=2, relief="flat", command=lambda t="%": self.set_value(t))
        self.btn3.grid(row=0, column=2, padx=(0,14), pady=14, ipadx=15, ipady=10)

        self.btn4=tk.Button(buttons_frame1, text="+", font=("Arial", 18), bg="LightPink4", fg="white", borderwidth=2, relief="flat", command=lambda t="+": self.set_value(t))
        self.btn4.grid(row=0, column=3, padx=(0,14), pady=14, ipadx=17, ipady=10)

        self.btn5=tk.Button(buttons_frame1, text="7", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="7": self.set_value(t))
        self.btn5.grid(row=1, column=0, padx=14, pady=(0,14), ipadx=18, ipady=10)

        self.btn6=tk.Button(buttons_frame1, text="8", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="8": self.set_value(t))
        self.btn6.grid(row=1, column=1, padx=(0,14), pady=(0,14), ipadx=18, ipady=10)

        self.btn7=tk.Button(buttons_frame1, text="9", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="9": self.set_value(t))
        self.btn7.grid(row=1, column=2, padx=(0,14), pady=(0,14), ipadx=18, ipady=10)

        self.btn8=tk.Button(buttons_frame1, text="-", font=("Arial", 18), bg="LightPink4", fg="white", borderwidth=2, relief="flat", command=lambda t="-": self.set_value(t))
        self.btn8.grid(row=1, column=3, padx=(0,14), pady=(0,14), ipadx=20, ipady=10)

        self.btn9=tk.Button(buttons_frame1, text="4", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="4": self.set_value(t))
        self.btn9.grid(row=2, column=0, padx=14, pady=(0,14), ipadx=18, ipady=10)

        self.btn10=tk.Button(buttons_frame1, text="5", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="5": self.set_value(t))
        self.btn10.grid(row=2, column=1, padx=(0,14), pady=(0,14), ipadx=18, ipady=10)

        self.btn11=tk.Button(buttons_frame1, text="6", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="6": self.set_value(t))
        self.btn11.grid(row=2, column=2, padx=(0,14), pady=(0,14), ipadx=18, ipady=10)

        self.btn12=tk.Button(buttons_frame1, text="x", font=("Arial", 18), bg="LightPink4", fg="white", borderwidth=2, relief="flat", command=lambda t="x": self.set_value(t))
        self.btn12.grid(row=2, column=3, padx=(0,14), pady=(0,14), ipadx=18, ipady=10)


        self.btn13=tk.Button(buttons_frame1, text="1", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="1": self.set_value(t))
        self.btn13.grid(row=3, column=0, padx=14, ipadx=18, ipady=10)

        self.btn14=tk.Button(buttons_frame1, text="2", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="2": self.set_value(t))
        self.btn14.grid(row=3, column=1, padx=(0,14), ipadx=18, ipady=10)

        self.btn15=tk.Button(buttons_frame1, text="3", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="3": self.set_value(t))
        self.btn15.grid(row=3, column=2, padx=(0,14), ipadx=18, ipady=10)

        self.btn16=tk.Button(buttons_frame1, text="÷", font=("Arial", 18), bg="LightPink4", fg="white", borderwidth=2, relief="flat", command=lambda t="÷": self.set_value(t))
        self.btn16.grid(row=3, column=3, padx=(0,14), ipadx=18, ipady=10)

        self.btn18=tk.Button(self, text="0", font=("Arial", 18), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t="0": self.set_value(t))
        self.btn18.pack(side="left", padx=16, ipadx=18, ipady=10)

        self.btn19=tk.Button(self, text=".", font=("Arial", 20, "bold"), bg="LightPink1", fg="black", borderwidth=2, relief="flat", command=lambda t=".": self.set_value(t))
        self.btn19.pack(side="left", padx=(0,16), ipadx=19, ipady=6)

        self.btn20=tk.Button(self, text="=", font=("Arial", 20, "bold"), bg="IndianRed4", fg="white", borderwidth=2, relief="flat", command=self.calculate)
        self.btn20.pack(side="left", padx=(0,16), ipadx=56, ipady=6)


    def set_value(self, char):
        if char=="AC":
            self.user_input.delete(0, tk.END)
        elif char=="Del":
            current_exp=self.user_input.get()
            self.user_input.delete(len(current_exp)-1, tk.END)
        else:
            self.user_input.insert(tk.END, char)

    def calculate(self):
        try:
            exp=self.user_input.get()
            exp = exp.replace("%", "/100")
            exp=exp.replace("x", "*")
            exp=exp.replace("÷", "/")
            result=eval(exp)
            self.user_input.delete(0, tk.END)
            self.user_input.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")

if __name__=="__main__":
    app=Calculator()
    app.mainloop()
