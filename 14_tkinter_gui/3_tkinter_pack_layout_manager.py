from textwrap import fill
import tkinter as tk

root = tk.Tk()
root.geometry('400x400')

lb_oben = tk.Label(root, text='Label oben', bg='green', fg='white')
lb_oben.pack(side='top', fill='x')

lb_unten = tk.Label(root, text='Label unten', bg='red', fg='white')
lb_unten.pack(side='bottom', fill='x')

lb_links = tk.Label(root, text='Label links', bg='blue', fg='white')
lb_links.pack(side='left', fill='y')

lb_rechts = tk.Label(root, text='Label rechts', bg='black', fg='white')
lb_rechts.pack(side='right', fill='y')



root.mainloop()