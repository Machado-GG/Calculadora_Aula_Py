import tkinter as tk
from tkinter import ttk, messagebox

class ToDoList_App:
    def __init__(self, root):
        self.root = root
        self.root.title('Lista de Tarefas')
        self.root.geometry('400x430')
        
        self.style = ttk.Style(root)
        self.style.configure('TButton', font=('Helvetica', 12), padding=3)


        self.label_list = tk.Label(root, text='Tarefas:', font=('Arial', 14))
        self.label_list.pack(pady=15)

        self.list = tk.Listbox(root, font=('Arial', 12), width=35)
        self.list.pack()
    
        self.btn_remove = ttk.Button(root, text='Remover tarefa', command=self.remove_task)
        self.btn_remove.pack(pady=10)

        self.label_task = tk.Label(root, text='Adicionar tarefa:', font=('Arial', 14))
        self.label_task.pack(pady=5)

        self.label_entry = ttk.Entry(root, width=30, font=('Arial', 12))
        self.label_entry.bind('<KeyPress>', self.shortcut)
        self.label_entry.pack(pady=10)

        self.btn_submit = ttk.Button(root, text='Adicionar tarefa', command=self.add_task)
        self.btn_submit.pack()

    def add_task(self):
        self.tasks = []
        userEntry = self.label_entry.get()

        if not userEntry:
            messagebox.showwarning(title='Alert', message='Campo vazio!')
        else:
            self.tasks.append(userEntry)
            self.label_entry.delete(0, tk.END) 

        for items in self.tasks:
            self.list.insert(tk.END, items) 

    def remove_task(self):
        selection = self.list.curselection()
        if not selection:
            messagebox.showinfo(title='Alert', message='Nenhuma tarefa selecionada')        
        elif selection == ():
            messagebox.showinfo(title='Alert', message='Nenhuma tarefa encontrada!')
        else:
            self.list.delete(selection)

    def shortcut(self, event):
        if event.state == 8 and event.keysym == 'Return':
            self.add_task()

root = tk.Tk()
app = ToDoList_App(root)
root.mainloop()