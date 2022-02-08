import tkinter as tk 

'''
bei jeder GUI muss man dafür sorgen, dass sich das Hauptfenster öffnet
Hauptfenster muss dann mit Widgets befüllt werden
z. B. label widget, button widget, entry widget, ... 
'''

root = tk.Tk() # Hauptfenster der GUI

# widget im Hauptfenster platzieren
label1 = tk.Label(root, text='Hallo tkinter Welt!')
label1.pack()

'''
Wenn Nutzer mit GUI interagiert, erkennt mainloop ein Event. 
Event: Nutzer klickt innerhalb der GUI (click)

x im Fenster beendet event loop
'''

root.mainloop() # tkinter event loop starten - damit man das Fenster sieht