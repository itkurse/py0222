import tkinter as tk

# Hauptfenster erstellen
root = tk.Tk()
root.geometry('800x400') # setze Fenster-Größe
root.minsize(width=300, height=300) # min size
root.maxsize(width=800, height=800) # max size 
root.resizable(width=True, height=False) # ob die Fenstergröße verändert werden darf
root.title('Fenster') # setze den Fenstertitel

lb1 = tk.Label(root, text='Mahlzeit!')
lb1.pack()

# event loop starten
root.mainloop()