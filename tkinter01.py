# # # pip install tkintertable
# from tkinter import *
# # main window object named root
# root = Tk()
# root.geometry("450x300")
# # calling mainloop method which is used
# # when your application is ready to run
# # and it tells the code to keep displaying
# mainloop()


# from tkinter import *
# root=Tk()
# root.geometry("450x300")

# lblname=Label(text='enter a name')
# txtname=Entry(font=('Arial', 16), width=20)
# lblage=Label(text='enter age')
# txtage=Entry(font=('Arial', 16), width=20)

# lblname.grid(row=0,column=0)
# txtname.grid(row=0,column=1)
# lblage.grid(row=1,column=0)
# txtage.grid(row=1,column=1)
# mainloop()

# from tkinter import *
# root =Tk()
# def callback():
#     lbllabel.configure(text="button clicked")
# root.geometry("450x300")
# lbllabel=Label(text='not clicked')
# btn=Button(text='click button',command=callback)

# lbllabel.grid(row=0,column=0)
# btn.grid(row=1,column=0)
# mainloop()

# from tkinter import *
# root=Tk()
# def callback():
#     global num_click
#     num_click=num_click+1
#     label.configure(text='clicked {} times'.format(num_click))
# num_click=0
# root.geometry("450x300")
# label=Label(text='button not clicked ')
# btn=Button(text="click me",command=callback)

# label.grid(row=0, column=0)
# btn.grid(row=1, column=0)

# mainloop()

# from tkinter import *
# def calculate():
#     temp=int(entry.get())
#     temp=9/5*temp+32
#     label.configure(text = 'Converted: {:.2f}'.format(temp))
#     entry.delete(0,END)
# root=Tk()
# root.geometry("650x500")

# message_label = Label(text='Enter a temperature',font=('Verdana', 16))
# label = Label(font=('Verdana', 16),width=20)
# entry = Entry(font=('Verdana', 16), width=20)
# calc_button = Button(text='Ok', font=('Verdana', 16),command=calculate)

# message_label.grid(row=0, column=0)
# entry.grid(row=0, column=1)
# calc_button.grid(row=0, column=2)
# label.grid(row=1, column=0,columnspan=3)

# mainloop()

