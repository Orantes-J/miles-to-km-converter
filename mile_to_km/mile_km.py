from tkinter import *
TITLE = "Mile to Km Converter"
FONT = ('Arial', 15, 'bold')

# WINDOW SETTINGS
window = Tk()
window.title(TITLE)
window.minsize(width=450, height=100)
window.config(padx=100)

# MILE ENTRY SETTING
mile_entry = Entry(width=20, text=0)
mile_entry.insert(END, string=0)
mile_entry.grid(row=0, column=1)

# MILE LABEL SETTING
mile_label = Label(text="Miles", font=FONT)
mile_label.grid(row=0, column=2)

# LABELS
prompt1 = Label(text="is equal to", font=FONT)
prompt1.grid(row=1, column=0)

prompt2 = Label(text=0, font=FONT)
prompt2.grid(row=1, column=1)


def button_clicked():
    km = int(mile_entry.get()) * 1.60934
    prompt2['text'] = km
    print(km)


prompt3 = Label(text='Km', font=FONT)
prompt3.grid(row=1, column=2)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(row=2, column=1)

window.mainloop()