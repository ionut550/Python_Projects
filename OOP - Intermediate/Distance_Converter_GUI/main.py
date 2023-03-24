import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx= 10, pady=10)

def converter():
    km = float(value.get())
    calculated_value = tkinter.Label(text=f"{km * 1.6}")
    calculated_value.grid(column=1,row=1)

#Entry
value = tkinter.Entry(width=7)
value.grid(column= 1, row= 0)

#Labels
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row= 0)
is_equal_to_label = tkinter.Label(text="is equal to ")
is_equal_to_label.grid(column=0 ,row=1)
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

#Button
button = tkinter.Button(text="Calculate",command=converter)
button.grid(column=1, row=2)
window.mainloop()