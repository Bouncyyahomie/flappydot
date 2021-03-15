from tkinter import * 
root = Tk()  
canv = Canvas(root, width=80, height=80, bg='white') 
canv.grid(row=2, column=3)  
img = PhotoImage(file=r"images/dot.gif") 
canv.create_image(20, 20, anchor=NW, image=img)  
mainloop()
