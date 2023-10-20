import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg

counter = 0

root = tk.Tk()
root.geometry("320x320")
root.title("BMI Rechner")
root.resizable(False, False)

def ausrechen(event=None):
    global counter
    try:
        gewicht = float(eingabe1.get())
        groesse = (float(eingabe2.get()) / 100) ** 2
        result = gewicht / groesse
        if counter > 0:
            resultlabel.pack_forget()
            counter = 0
        resultlabel.configure(text=round(result, 2))
        resultlabel.pack(side="top", fill="x", padx=5, pady=2)
        counter += 1
    except:
        resultlabel.pack_forget()
        msg.showerror("Error", '''Etwas ist schief gelaufen, bitte versuchen Sie es noch einmal.
        Es müssen alle Felder mit Zahlen ausgefüllt werden.''')



label1 = ttk.Label(root, text="Bitte gebe dein Gewicht in Kg an")
label1.pack(side="top", fill="x", padx=5, pady=2)

eingabe1 = ttk.Entry(root, width=50)
eingabe1.pack(side="top", fill="x", padx=5, pady=2)
eingabe1.bind('<Return>', ausrechen)

label2 = ttk.Label(root, text="Bitte gebe deine grösse in cm an")
label2.pack(side="top", fill="x", padx=5, pady=2)

eingabe2 = ttk.Entry(root)
eingabe2.pack(side="top", fill="x", padx=5, pady=2)
eingabe2.bind('<Return>', ausrechen)

get_result = ttk.Button(root, command=ausrechen, text="Resultat")
get_result.pack(side="top", fill="x", padx=5, pady=2)

# Create the result label once and leave it empty
resultlabel = ttk.Label(root, text="")

root.mainloop()