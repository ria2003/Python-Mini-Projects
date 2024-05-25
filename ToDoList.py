import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from ttkbootstrap import Style
from PIL import Image, ImageTk
import json

class ToDoList(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ToDo List")
        self.geometry("500x550")
        
        #Creating label for the app
        self.header_label=ttk.Label(self, text="To-Do List", font=("Brush Script MT", "28"), foreground="#FFFFF0")   
        self.header_label.pack(padx=10, pady=(15,0)) 

        # Creating and configuring a custom style for the entry widget
        style=Style(theme="darkly")
        style.configure("Custom.TEntry", fieldbackground="#FFFFF0", foreground="black")

        # Creating a frame to hold the entry and button
        input_frame = tk.Frame(self)
        input_frame.pack(padx=30, pady=(15, 15), fill=tk.X)
        input_frame.grid_columnconfigure(0, weight=1)

        # Creating an input field for adding tasks with the custom style
        self.input_task=ttk.Entry(input_frame, font=("Courier New", 14), style="Custom.TEntry", width=34)
        self.input_task.grid(row=0, column=0, sticky="ew")

        #Setting placeholder for input_task
        self.input_task.insert(0,"Enter your task")

        #Binding the placeholder with function when the input field is clicked
        self.input_task.bind("<FocusIn>",self.clear_placeholder)

        #Binding the placeholder with function when the input field loses focus
        self.input_task.bind("<FocusOut>",self.fill_placeholder)

        #Creating Label with an image and binding it with a function to add tasks
        self.img=Image.open(r'C:\Users\HP\Downloads\plus.png')
        self.image=self.img.resize((40, 40))
        self.add_img=ImageTk.PhotoImage(self.image)
        self.add_btn=ttk.Label(input_frame, image=self.add_img)
        self.add_btn.grid(row=0, column=1, sticky="ew", padx=10)
        self.add_btn.bind("<Button-1>",self.add_task)

        #Creating Listbox to display the tasks
        self.disp_task=tk.Listbox(self, font=("Courier New", 16),height=2, selectmode=tk.NONE)
        self.disp_task.pack(padx=30, pady=15, ipadx=2, ipady=2, expand=True, fill=tk.BOTH)
        self.disp_task.config(bg="#FFFFF0", fg="black")

        #Creating Label with an image and binding it with a function to edit tasks
        self.img1=Image.open(r'C:\Users\HP\Downloads\pen.png')
        self.image1=self.img1.resize((40, 40))
        self.edit_img=ImageTk.PhotoImage(self.image1)
        self.edit_btn=ttk.Label(self, image=self.edit_img)
        self.edit_btn.pack(side="left", padx=15, pady=(0,15), expand=True)
        self.edit_btn.bind("<Button-1>",self.edit_task)

        #Creating Label with an image and binding it with a function to mark the tasks as completed
        self.img4=Image.open(r'C:\Users\HP\Downloads\checklist.png')
        self.image4=self.img4.resize((45, 45))
        self.done_img=ImageTk.PhotoImage(self.image4)
        self.done_btn=ttk.Label(self, image=self.done_img)
        self.done_btn.pack(side="left", pady=(0,20), expand=True)
        self.done_btn.bind("<Button-1>",self.task_done)

        #Creating Label with an image and binding it with a function to delete the tasks 
        self.img2=Image.open(r'C:\Users\HP\Downloads\bin.png')
        self.image2=self.img2.resize((40, 40))
        self.del_img=ImageTk.PhotoImage(self.image2)
        self.del_btn=ttk.Label(self, image=self.del_img)
        self.del_btn.pack(side="left", padx=15, pady=(0,15), expand=True)
        self.del_btn.bind("<Button-1>",self.delete_task)

        #Creating Label with an image and binding it with a function to track the tasks
        self.img3=Image.open(r'C:\Users\HP\Downloads\pie-chart.png')
        self.image3=self.img3.resize((40, 40))
        self.stats_img=ImageTk.PhotoImage(self.image3)
        self.stats_btn=ttk.Label(self, image=self.stats_img)
        self.stats_btn.pack(side="left", padx=(0,15), pady=(0,20), expand=True)
        self.stats_btn.bind("<Button-1>",self.task_stats)

        # Creating tooltips for the Labels
        self.create_tooltip(self.add_btn, "Add Task")
        self.create_tooltip(self.edit_btn, "Edit Task")
        self.create_tooltip(self.done_btn, "Mark Task as Done")
        self.create_tooltip(self.del_btn, "Delete Task")
        self.create_tooltip(self.stats_btn, "Task Statistics")

        self.load_tasks()


    def create_tooltip(self, widget, text):
        def show_tooltip(event):
            x, y, _, _ = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 25

            tooltip = tk.Toplevel(widget)
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{x}+{y}")
            label = tk.Label(tooltip, text=text, relief="solid", borderwidth=1)
            label.config(bg="#FFFFF0", fg="black")
            label.pack()

            # Bind a function to destroy the tooltip when leaving the widget
            widget.bind("<Leave>", lambda e: tooltip.destroy())

        widget.bind("<Enter>", show_tooltip)
        
    def clear_placeholder(self,event):
        if self.input_task.get()=="Enter your task":
            self.input_task.delete(0,tk.END)
            self.input_task.configure(style="Custom.TEntry")

    def fill_placeholder(self,event):
        if self.input_task.get()=="":
            self.input_task.insert(0,"Enter your task")
            self.input_task.configure(style="Custom.TEntry")

    def add_task(self, event=None):
        task=self.input_task.get()
        if task!= "Enter your task":
            self.disp_task.insert(tk.END,task)
            self.disp_task.itemconfig(tk.END, fg="orange")
            self.input_task.delete(0,tk.END)
            self.save_task()

    def save_task(self):
        data=[]
        for i in range(self.disp_task.size()):
            text=self.disp_task.get(i)
            color=self.disp_task.itemcget(i, "fg")
            data.append({"text":text, "color":color})
        with open("tasks.json","w") as f:
            json.dump(data,f)
            
    def load_tasks(self):
        try:
            with open("tasks.json","r") as f:
                data=json.load(f)
                for task in data:
                    self.disp_task.insert(tk.END, task["text"])
                    self.disp_task.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass

    def edit_task(self, event=None):
        selected_task=self.disp_task.curselection()
        if selected_task:
            current_task=self.disp_task.get(selected_task)
            new_task=simpledialog.askstring("Edit Task","Enter new task: ",initialvalue=current_task)
            if new_task:
                self.disp_task.delete(selected_task)
                self.disp_task.insert(selected_task,new_task)
                self.disp_task.itemconfig(selected_task, fg="orange")
                self.save_task()

    def delete_task(self, event=None):
        selected_task=self.disp_task.curselection()
        if selected_task:
            self.disp_task.delete(selected_task)
            self.save_task()

    def task_done(self, event=None):
        selected_task=self.disp_task.curselection()
        if selected_task:
            self.disp_task.itemconfig(selected_task,fg="green")
            self.save_task()

    def task_stats(self, event=None):
        completed_count=0
        total_tasks=self.disp_task.size()
        for i in range(total_tasks):
            if self.disp_task.itemcget(i,"fg")=="green":
                completed_count+=1
        pending_tasks=total_tasks-completed_count
        messagebox.showinfo("Task statistics",f"Total tasks: {total_tasks} \nCompleted tasks: {completed_count} \nPending tasks: {pending_tasks}")
        

if __name__ == '__main__':
    app = ToDoList()
    app.mainloop()
