import tkinter as tk
from tkinter import ttk, messagebox

class BMICalculator:   
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")
        self.root.geometry('300x150')
        self.label_weight = tk.Label(root, text="Peso (kg):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(root)
        self.entry_weight.pack()
        self.label_height = tk.Label(root, text="Altura (m):")
        self.label_height.pack()
        self.entry_height = tk.Entry(root)
        self.entry_height.pack()
        self.button_calculate = ttk.Button(root, text="Calcular IMC", command=self.calculate_BMI)
        self.button_calculate.pack(pady=10)
        
    def calculate_BMI(self):
        weight = float(self.entry_weight.get())
        height = float(self.entry_height.get())
        imc = weight / (height ** 2)
        result = f"Seu IMC é: {imc:.2f}"
        messagebox.showinfo(title='Resultado', message=f'{result} | Classificação: {self.show_BMI_category(imc)}')
    
    def show_BMI_category(self, value):
        if value < 18.5:
            return 'Magreza'
        elif value >= 18.5 and value <= 24.9:
            return 'Normal'
        elif value >= 25 and value <= 29.9:
            return 'Sobrepeso'
        else:
            return 'Obesidade'

root = tk.Tk()
app = BMICalculator(root)
root.mainloop()
