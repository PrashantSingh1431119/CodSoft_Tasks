import tkinter as tk
from tkinter import messagebox

def new_task():
    task=entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.dete(0, tk.END)
    else:
        messagebox.showwarning("Alert", "Please! Enter your task.")

def delete_task():
    selected_task=listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)
def clean_task():
    listbox.delete(0, tk.END)
def task_done():
    selected_task=listbox.curselection()
    if selected_task:
        task_index=selected_task[0]
        task=listbox.get(task_index)
        listbox.itemconfig(task_index,{'bg': 'light green'})
        done_listbox.insert(tk.END, task)
        listbox.delete(task_index)
        
root=tk.Tk()
root.title("Today's Task")

entry=tk.Entry(root, font=('Seouge', 16))
new_button=tk.Button(root, text='Add Task', command=new_task)
delete_button=tk.Button(root, text="Delete Selected", command=delete_task)
clean_button=tk.Button(root, text="Clear All Tasks", command=clean_task)
task_done_button=tk.Button(root, text="Task Completed", command=task_done)

listbox=tk.Listbox(root, font=('seouge', 16 ), selectmode=tk.SINGLE)
done_listbox=tk.Listbox(root, font=('seouge', 16), selectmode=tk.SINGLE)

entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12)
new_button.grid(row=0, column=3, padx=12, pady=12)
delete_button.grid(row=1, column=0, padx=12, pady=12)
clean_button.grid(row=1, column=1, padx=12, pady=12)
task_done_button.grid(row=1, column=2, padx=12, pady=12)
listbox.grid(row=2, column=0, padx=12, pady=12, sticky='nsew')
done_listbox.grid(row=2, column=2, padx=12, pady=12, sticky='nsew')

root.grid_rowconfigure(2, weight=2)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(2, weight=2)

root.mainloop()