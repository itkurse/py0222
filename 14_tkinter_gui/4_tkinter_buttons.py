import tkinter as tk


def button_click():
    # was steht momentan im Label drinn?
    click_counter = int(label1['text'])
    click_counter += 1
    label1['text'] = str(click_counter)



root = tk.Tk()
root.geometry('400x400')

button1 = tk.Button(root, text='Klick mich!', command=button_click)
button1.pack()

button2 = tk.Button(root, text='Programm beenden', command=root.destroy)
button2.pack()

label1 = tk.Label(root, text='')
label1.pack()

root.mainloop()