import tkinter as tk
from tkinter import ttk, messagebox
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title('Cronômetro')
        self.root.geometry('300x100')

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.label = tk.Label(root, text='0.00', font=('Helvetica', 14))
        self.label.grid(row=0, column=1, sticky='nsew', pady=10)

        self.start_btn = ttk.Button(root, text='Iniciar', command=self.start_timer)
        self.start_btn.grid(row=1, column=0, pady=20)
        self.stop_btn = ttk.Button(root, text='Parar', command=self.stop_timer)
        self.stop_btn.grid(row=1, column=1, pady=20)
        self.reset_btn = ttk.Button(root, text='Reset', command=self.reset_timer)
        self.reset_btn.grid(row=1, column=2, pady=20)

        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            self.current_time = time.time()
            elapsed_time = self.current_time - self.time_start
            self.label.config(text=f'{elapsed_time:.2f}')
            self.root.after(100, self.update_timer)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.time_start = time.time()
            self.update_timer()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False


    def reset_timer(self):
        if self.timer_running:
            messagebox.showwarning(title='Alert!', message='Pause antes de reiniciar!')
        else:
            self.label.config(text='0.00')
            self.timer_running = False
                  

main = tk.Tk()
app = Stopwatch(main)
main.mainloop()