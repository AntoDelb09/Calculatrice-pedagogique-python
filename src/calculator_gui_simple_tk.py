# calculator_gui_simple_tk.py - Version Tkinter simplifiée sans emojis
import tkinter as tk
from tkinter import messagebox
from calculator import add, subtract, multiply, divide

class SimpleCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculatrice Python")
        self.root.geometry("350x400")

        # Variables
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.operation_var = tk.StringVar(value="+")

        self.create_widgets()

    def create_widgets(self):
        # Titre
        tk.Label(self.root, text="Calculatrice Python", font=("Arial", 16, "bold")).pack(pady=10)

        # Premier nombre
        frame1 = tk.Frame(self.root)
        frame1.pack(pady=5)
        tk.Label(frame1, text="Nombre 1:").pack(side=tk.LEFT)
        tk.Entry(frame1, textvariable=self.num1_var, width=15).pack(side=tk.LEFT, padx=10)

        # Operation
        frame2 = tk.Frame(self.root)
        frame2.pack(pady=5)
        tk.Label(frame2, text="Operation:").pack(side=tk.LEFT)
        operations = ["+", "-", "*", "/"]
        for op in operations:
            tk.Radiobutton(frame2, text=op, variable=self.operation_var, value=op).pack(side=tk.LEFT)

        # Deuxième nombre
        frame3 = tk.Frame(self.root)
        frame3.pack(pady=5)
        tk.Label(frame3, text="Nombre 2:").pack(side=tk.LEFT)
        tk.Entry(frame3, textvariable=self.num2_var, width=15).pack(side=tk.LEFT, padx=10)

        # Bouton Calculer
        tk.Button(self.root, text="Calculer", command=self.calculate, bg="green", fg="white").pack(pady=10)

        # Resultat
        tk.Label(self.root, text="Resultat:").pack()
        tk.Label(self.root, textvariable=self.result_var, font=("Arial", 14, "bold"), fg="blue").pack(pady=5)

        # Bouton Effacer
        tk.Button(self.root, text="Effacer", command=self.clear, bg="red", fg="white").pack(pady=5)

    def calculate(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            op = self.operation_var.get()

            if op == '+':
                result = add(num1, num2)
            elif op == '-':
                result = subtract(num1, num2)
            elif op == '*':
                result = multiply(num1, num2)
            elif op == '/':
                result = divide(num1, num2)

            self.result_var.set(f"{num1} {op} {num2} = {result}")
            messagebox.showinfo("Resultat", f"Le resultat est: {result}")

        except ValueError:
            messagebox.showerror("Erreur", "Entrez des nombres valides!")
        except ZeroDivisionError:
            messagebox.showerror("Erreur", "Division par zero impossible!")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur: {e}")

    def clear(self):
        self.num1_var.set("")
        self.num2_var.set("")
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCalculatorGUI(root)
    root.mainloop()