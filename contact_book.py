import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from validate_email import validate_email
import json

class ContactBook(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.geometry("700x690")
        self.configure(bg="white")

        title_frame = tk.Frame(self, bg="white")
        title_frame.pack(fill=tk.X)

        self.lbl=tk.Label(title_frame, text="Contact Book", font=("Cooper Black", 24,"italic"), bg="white", fg="black")
        self.lbl.pack(pady=15, padx=(210,20), side="left")

        self.img=Image.open(r'C:\Users\HP\Downloads\contacts.png')
        self.image=self.img.resize((30, 30))
        self.add_img=ImageTk.PhotoImage(self.image)
        self.lbl2=ttk.Label(title_frame, image=self.add_img, background="white")
        self.lbl2.pack(pady=10, side="left")

        input_frame = tk.Frame(self, bg="white")
        input_frame.pack(fill=tk.X)
        input_frame.grid_columnconfigure(0, weight=1)

        self.name=tk.Entry(input_frame, font=("Arial", 11), fg="black", bg="LavenderBlush1", justify="center")
        self.name.grid(ipadx=64, ipady=6, pady=(0,20), row=0, column=0)
        self.name.insert(0, "Enter name: ")
        self.name.bind("<FocusIn>", self.clear_placeholder_name)
        self.name.bind("<FocusOut>", self.fill_placeholder_name)

        self.phone=tk.Entry(input_frame, font=("Arial", 11), fg="black", bg="LavenderBlush1", justify="center")
        self.phone.grid(ipadx=64, ipady=6, pady=(0,20), padx=(0,38), row=0, column=1)
        self.phone.insert(0, "Enter phone number: ")
        self.phone.bind("<FocusIn>", self.clear_placeholder_phone)
        self.phone.bind("<FocusOut>", self.fill_placeholder_phone)

        self.email=tk.Entry(input_frame, font=("Arial", 11), fg="black", bg="LavenderBlush1", justify="center")
        self.email.grid(ipadx=64, ipady=6, pady=(0,20), row=1, column=0)
        self.email.insert(0, "Enter email id: ")
        self.email.bind("<FocusIn>", self.clear_placeholder_email)
        self.email.bind("<FocusOut>", self.fill_placeholder_email)

        self.address=tk.Entry(input_frame, font=("Arial", 11), fg="black", bg="LavenderBlush1", justify="center")
        self.address.grid(ipadx=64, ipady=6, pady=(0,20), padx=(0,38), row=1, column=1)
        self.address.insert(0, "Enter address: ")
        self.address.bind("<FocusIn>", self.clear_placeholder_address)
        self.address.bind("<FocusOut>", self.fill_placeholder_address)

        self.add_btn=tk.Button(self, text="Add", bg="orchid4", fg="white", font=("Cooper Black", 12), command=self.add_contact)
        self.add_btn.pack(ipadx=30, pady=(0,20))

        style = ttk.Style()
        style.configure("Custom.Treeview", 
                        font=("Arial", 10), 
                        foreground="black", 
                        rowheight=25, 
                        background="LavenderBlush1",
                        fieldbackground="LavenderBlush1")
        
        style.configure("Custom.Treeview.Heading", 
                        font=("Arial", 10, "bold"), 
                        foreground="black", 
                        )
        
        search_frame = tk.Frame(self, bg="white")
        search_frame.pack(fill=tk.X)

        self.search_entry=tk.Entry(search_frame, bg="LavenderBlush1", fg="black", font=("Arial", 11), width=72, justify="center")
        self.search_entry.pack(side="left", ipady=6, padx=(35,15))
        self.search_entry.insert(0, "Search by name or phone")
        self.search_entry.bind("<FocusIn>", self.clear_placeholder_search)
        self.search_entry.bind("<FocusOut>", self.fill_placeholder_search)
        
        self.img2=Image.open(r'C:\Users\HP\Downloads\search-user.png')
        self.image2=self.img2.resize((32,32))
        self.add_img2=ImageTk.PhotoImage(self.image2)
        self.search_btn=ttk.Label(search_frame, image=self.add_img2, background="white")
        self.search_btn.pack(side="left")
        self.search_btn.bind("<Button-1>",self.search_contact)

        self.contact_list = ttk.Treeview(self, columns=("name", "phone", "email", "address"), show='headings', height=1, style="Custom.Treeview")
        self.contact_list.heading("name", text="Name")
        self.contact_list.heading("phone", text="Phone")
        self.contact_list.heading("email", text="Email")
        self.contact_list.heading("address", text="Address")
        self.contact_list.column('name', width=20, anchor='center')
        self.contact_list.column('phone', width=1, anchor='center')
        self.contact_list.column('email', width=60, anchor='center')
        self.contact_list.column('address', width=80, anchor='center')
        self.contact_list.pack(padx=35, pady=(20,20), expand=True, fill=tk.BOTH)

        self.view_btn=tk.Button(self, text="View", bg="orchid4", fg="white", font=("Cooper Black", 12), width=10, command=self.view_contacts)
        self.view_btn.pack(side="left",expand=True, pady=(0,20), padx=(60,0))

        self.update_btn=tk.Button(self, text="Update", bg="orchid4", fg="white", font=("Cooper Black", 12), width=10, command=self.edit_contact)
        self.update_btn.pack(side="left",expand=True, pady=(0,20))

        self.delete_btn=tk.Button(self, text="Delete", bg="orchid4", fg="white", font=("Cooper Black", 12), width=10, command=self.delete_contact)
        self.delete_btn.pack(side="left",expand=True, pady=(0,20), padx=(0, 60))

        self.load_contacts()
    

    def clear_placeholder_name(self, event):
        if self.name.get()=="Enter name: ":
            self.name.delete(0, tk.END)
            self.name.configure(font=("Arial", 11), fg="black", bg="LavenderBlush1")


    def clear_placeholder_phone(self, event):
        if self.phone.get()=="Enter phone number: ":
            self.phone.delete(0, tk.END)
            self.phone.configure(font=("Arial", 11), fg="black", bg="LavenderBlush1") 


    def clear_placeholder_email(self, event): 
        if self.email.get()=="Enter email id: ":
            self.email.delete(0, tk.END)
            self.email.configure(font=("Arial", 11), fg="black", bg="LavenderBlush1")


    def clear_placeholder_address(self, event):
        if self.address.get()=="Enter address: ":
            self.address.delete(0, tk.END)
            self.address.configure(font=("Arial", 11), fg="black", bg="LavenderBlush1")

    
    def clear_placeholder_search(self, event):
        if self.search_entry.get() == "Search by name or phone":
            self.search_entry.delete(0, tk.END)
            self.search_entry.configure(bg="LavenderBlush1", fg="black", font=("Arial", 11))


    def fill_placeholder_name(self,event):
        if self.name.get()=="":
            self.name.insert(0, "Enter name: ")
            self.name.configure(font=("Arial", 11), fg="black", bg="LavenderBlush1")


    def fill_placeholder_phone(self,event):
        if self.phone.get()=="":
            self.phone.insert(0, "Enter phone number: ")
            self.phone.configure(font=("Arial", 11), fg="black", bg="LavenderBlush1")


    def fill_placeholder_email(self,event):
        if self.email.get()=="":
            self.email.insert(0, "Enter email id: ")
            self.email.configure(font=("Arial", 11), fg="black", bg="LavenderBlush1")


    def fill_placeholder_address(self,event):
        if self.address.get()=="":
            self.address.insert(0, "Enter address: ")
            self.address.configure(font=("Arial", 11), fg="black", bg="LavenderBlush1")


    def fill_placeholder_search(self, event):
        if self.search_entry.get() == "":
            self.search_entry.insert(0, "Search by name or phone")
            self.search_entry.configure(bg="LavenderBlush1", fg="black", font=("Arial", 11))

    
    def add_contact(self):
        name=self.name.get()
        phone=self.phone.get()
        email=self.email.get()
        address=self.address.get()

        if name and phone and email and address and name != "Enter name: " and phone != "Enter phone number: " and email != "Enter email id: " and address != "Enter address: ":
            if phone.isdigit() and validate_email(email)==True:
                self.contact_list.insert('', tk.END, values=(name, phone, email, address))
                self.name.delete(0, tk.END)
                self.phone.delete(0, tk.END)
                self.email.delete(0, tk.END)
                self.address.delete(0, tk.END)
                self.save_contacts()
            else:
                messagebox.showerror("Error", "Invalid phone number or email id")
        else:
            messagebox.showerror("Error", "Please fill out all fields")


    def save_contacts(self):
        data = []
        for child in self.contact_list.get_children():
            item = self.contact_list.item(child)
            values = item['values']
            data.append({
                "name": values[0],
                "phone": values[1],
                "email": values[2],
                "address": values[3]
            })

        with open("contacts.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_contacts(self):
        try:
            with open("contacts.json","r") as f:
                data=json.load(f)
                for contact in data:
                    self.contact_list.insert('', tk.END, values=(contact["name"], contact["phone"], contact["email"], contact["address"]))
        except FileNotFoundError:
            pass

    
    def search_contact(self, event):
        query = self.search_entry.get()
        if query == "Search by name or phone":
            return

        for item in self.contact_list.get_children():
            self.contact_list.delete(item)

        try:
            with open("contacts.json", "r") as f:
                data = json.load(f)
                for contact in data:
                    if query.lower() in contact["name"].lower() or query in str(contact["phone"]):
                        self.contact_list.insert('', tk.END, values=(contact["name"], contact["phone"], contact["email"], contact["address"]))
        except FileNotFoundError:
            pass

    
    def view_contacts(self):
        for item in self.contact_list.get_children():
            self.contact_list.delete(item)

        try:
            with open("contacts.json","r") as f:
                data=json.load(f)
                for contact in data:
                    self.contact_list.insert('', tk.END, values=(contact["name"], contact["phone"], contact["email"], contact["address"]))
        except FileNotFoundError:
            pass
    

    def edit_contact(self):
        selected_item = self.contact_list.selection()
        if selected_item:
            item = self.contact_list.item(selected_item)
            current_contact = item['values']

            edit = tk.Toplevel(self)
            edit.title("Edit Contact")
            edit.geometry('400x280')
            edit.configure(bg="white")

            tk.Label(edit, text="Name:", font=("Arial", 11), bg="white").grid(row=0, column=0, pady=(30,15), padx=(15,20))
            new_name = tk.Entry(edit, font=("Arial", 11), fg="black", bg="LavenderBlush1", justify="center", width=34)
            new_name.grid(row=0, column=1, pady=(30, 15), ipady=5)
            new_name.insert(0, current_contact[0])

            tk.Label(edit, text="Phone:", font=("Arial", 11), bg="white").grid(row=1, column=0, pady=(0,15), padx=(15,20))
            new_phone = tk.Entry(edit, font=("Arial", 11), fg="black", bg="LavenderBlush1", justify="center", width=34)
            new_phone.grid(row=1, column=1, pady=(0,15), ipady=5)
            new_phone.insert(0, current_contact[1])

            tk.Label(edit, text="Email:", font=("Arial", 11), bg="white").grid(row=2, column=0, pady=(0,15), padx=(15,20))
            new_email = tk.Entry(edit, font=("Arial", 11), fg="black", bg="LavenderBlush1", justify="center", width=34)
            new_email.grid(row=2, column=1, pady=(0,15), ipady=5)
            new_email.insert(0, current_contact[2])

            tk.Label(edit, text="Address:", font=("Arial", 11), bg="white").grid(row=3, column=0, pady=(0,15), padx=(15,20))
            new_address = tk.Entry(edit, font=("Arial", 11), fg="black", bg="LavenderBlush1", justify="center", width=34)
            new_address.grid(row=3, column=1, pady=(0,15), ipady=5)
            new_address.insert(0, current_contact[3])

            def update_contact():
                name = new_name.get()
                phone = new_phone.get()
                email = new_email.get()
                address = new_address.get()

                if name and phone and email and address:
                    if phone.isdigit() and validate_email(email):
                        self.contact_list.item(selected_item, values=(name, phone, email, address))
                        self.save_contacts()
                        edit.destroy()
                        messagebox.showinfo("Update Contact", "Contact updated successfully!")
                    else:
                        messagebox.showerror("Error", "Invalid phone number or email id")
                else:
                    messagebox.showerror("Error", "Please fill out all fields")

            ok_btn = tk.Button(edit, text="OK", bg="orchid4", fg="white", font=("Cooper Black", 12), command=update_contact, width=8)
            ok_btn.grid(row=4, column=1, padx=(0,75), pady=10)


    def delete_contact(self):
        selected_item = self.contact_list.selection()
        if selected_item:
            confirm=messagebox.askokcancel("Delete Contact", "Do you want to delete contact?")
            if confirm:
                self.contact_list.delete(selected_item)
                self.save_contacts()


if __name__=="__main__":
    app=ContactBook()
    app.mainloop()