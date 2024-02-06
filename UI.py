import tkinter as tk

root=tk.Tk()
root.geometry("800x500")
root.title("Acceso base datos")
label=tk.Label(root,text="Introduzca su usuario", font=('arial',18))
label.pack(padx=20,pady=20)
textbox=tk.Text(root,font=('Arial',16),height=1)
textbox.pack(padx=30)
button=tk.Button(root,text="Log-in",font=('Arial',18))
button.pack(pady=10)

root.mainloop()