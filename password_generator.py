import tkinter as tk
import random
import string
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

class PassGenerator(ThemedTk):
    def __init__(self):
        super().__init__()
        
        # Set the theme using ttkthemes
        self.set_theme("alt")

        self.title("Random Password Generator")
        self.geometry("500x300")

        # Creating label for the app
        self.heading = ttk.Label(self, text="  Password Generator  ", font=("Cooper Black", 22))
        self.heading.pack(padx=15, pady=27, ipady=2)

        # Creating entry widget to enter length of password
        self.pass_length = ttk.Entry(self, font=("Courier New", 16), justify='center')
        self.pass_length.pack(padx=82, ipady=3, pady=(0,30), fill=tk.X)

        #Setting placeholder for input_task
        self.pass_length.insert(0,"Enter password length")

        #Binding the placeholder with function when the input field is clicked
        self.pass_length.bind("<FocusIn>",self.clear_placeholder)

        #Binding the placeholder with function when the input field loses focus
        self.pass_length.bind("<FocusOut>",self.fill_placeholder)

        # Create and configure a custom style for the button
        style = ttk.Style(self)
        style.configure("Custom.TButton", font=("Courier New", 16))

        # Creating a frame to hold the buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=(0,30), fill=tk.X)

        # Creating the "Generate" button
        self.btn_generate = ttk.Button(button_frame, text="Generate", command=self.generate_password, style="Custom.TButton", cursor="hand2", takefocus=False)
        self.btn_generate.pack(side='left', expand=True, ipady=3)

        # Creating the "Copy" button to copy the password to the clipboard
        self.btn_copy = ttk.Button(button_frame, text="Copy", command=self.copy_password, style="Custom.TButton", cursor="hand2", takefocus=False)
        self.btn_copy.pack(side='left', expand=True,  ipady=3)

        # Creating Label to display the generated password
        self.pwd = ttk.Label(self, font=("Courier New", 16), background="gray94")
        self.pwd.pack(padx=15, pady=(0,30), ipady=2)

    def clear_placeholder(self, event):
        if self.pass_length.get()=="Enter password length":
            self.pass_length.delete(0,tk.END)

    def fill_placeholder(self, event):
        if self.pass_length.get()=="":
            self.pass_length.insert(0,"Enter password length")
    
    def generate_password(self):
        pwd_len = self.pass_length.get()
        if pwd_len.isdigit() and (int(pwd_len))>=1:  
            characters = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choice(characters) for i in range(int(pwd_len)))
            self.pwd.config(text=password)  
        else:
            self.pwd.config(text="  Enter a valid password length  ")

    def copy_password(self):
        password = self.pwd.cget("text")
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            messagebox.showinfo("Password Copied", "Password copied to clipboard.")

if __name__ == '__main__':
    app = PassGenerator()
    app.mainloop()
