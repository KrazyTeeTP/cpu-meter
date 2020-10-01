from tkinter import *
import psutil

root = Tk()
root.title('CPU Meter')
root.geometry('500x500')

def cpu():
	a = psutil.cpu_percent()
	# label.config(text=f'CPU: {a:02.0f}%')
	label.config(text=f'CPU: {a:02.0f}%')
	label.after(800, cpu)


label = Label(root, font=('arial', 55), bg='black', fg='white')
label.pack(fill=BOTH, expand=True)

cpu()

root.mainloop()