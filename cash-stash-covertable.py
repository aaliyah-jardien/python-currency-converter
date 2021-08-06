from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

window = Tk()

# STRINGVAR
results = StringVar()
values1 = StringVar()
values2 = StringVar()

# WINDOW FEATURES
window.geometry("850x750")
window.title("Aaliyah's Currency Converter")
window.config(bg="#27323A")
window.resizable(0, 0)

# ADDING IMAGE
krooning = PhotoImage(file="wage-3.png")
canvas = Canvas(window, width=1000, height=450, highlightthickness="0")
canvas.create_image(0, 0, anchor=NW, image=krooning)
canvas.config(bg='#27323A')
canvas.place(x=-78, y=25)

# LABELS
instr = Label(window, text="                    Please select your currencies below to proceed                          ", font="arial 15 italic", bg="#27323A", fg="#EF3433")
instr.place(x=0, y=430)

heading = Label(window, text="        CURRENCY CONVERTER      ", font="arial 33 bold italic", bg="#27323A", fg="#FFFDFE")
heading.place(x=-10, y=2)

fromm = Label(window, text="FROM: ", font="arial 20 bold italic", bg="#27323A", fg="#FFFDFE")
fromm.place(x=150, y=465)

to = Label(window, text="TO: ", font="arial 20 bold italic", bg="#27323A", fg="#FFFDFE")
to.place(x=150, y=500)

enter = Label(window, text="ENTER YOUR AMOUNT: ", font="arial 20 bold italic", bg="#27323A", fg="#FFFDFE")
enter.place(x=150, y=535)


# Label(window, text='Enter Amount:', bg="#27323A").place(x=65, y=330)
# ent1 = Entry(window, bg='white')
# ent1.place(x=200, y=330)
# ent1.focus()
# Label(window, text='Converted Amount:', bg='#27323A').place(x=65, y=380)
# Label(window, text='', textvariable=results, bg='#27323A').place(x=200, y=380)

# GETTING CURRENCY CONVERTER API
# information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
# information_json = information.json()
#
# conversion_rates = information_json['conversion_rates']
#
# currency = []
# for i in conversion_rates.keys():
#     currency.append(i)
#
# currency2 = []
# for i in conversion_rates.keys():
#     currency2.append(i)
#
# currency_cb = ttk.Combobox(window)
# currency_cb['values'] = currency
# currency_cb['state'] = 'readonly'
# currency_cb.set('Select Currency')
# currency_cb.place(x=10, y=280)
#
#
# currency_cb2 = ttk.Combobox(window)
# currency_cb2['values'] = currency2
# currency_cb2['state'] = 'readonly'
# currency_cb2.set('Select Currency')
# currency_cb2.place(x=253, y=280)

# FUNCTIONS
# def convert(from_currency, to_currency, amount):
#     # first convert it into USD if it is not in USD.
#     # because our base currency is USD
#     if from_currency != 'USD':
#         amount = amount / conversion_rates[from_currency]
#
#     amount = round(amount * conversion_rates[to_currency], 4)
#     return amount
#
#
# def perform():
#     try:
#         amount = float(ent1.get())
#         from_curr = currency_cb.get()
#         to_curr = currency_cb2.get()
#
#         converted_amount = convert(from_curr, to_curr, amount)
#
#         results.set(converted_amount)
#     except ValueError:
#         if ent1 != int and ent1 != float:
#             messagebox.showerror('Entry not valid', 'Enter numbers only')
#
#     except requests.exceptions.ConnectionError:
#         messagebox.showerror('Internet error', 'Internet Bad')
#     except KeyError:
#         messagebox.showerror('ERROR!!!!!!!!!!!!!!!', 'Select Currency')
#
#
# def kill():
#     return window.destroy()
#
#
# def clear():
#     currency_cb.set('Select Currency')
#     currency_cb2.set('Select Currency')
#     ent1.delete(0, END)
#     ent1.focus()
#     results.set('')

# BUTTONS
# Button(window, text="CLEAR", borderwidth=3, bg='white', command=perform).place(x=180, y=430)
# Button(window, text="CONVERT", borderwidth=3, bg='white', command=kill).place(x=281, y=480)
# Button(window, text="EXIT", borderwidth=3, bg='white', command=clear).place(x=100, y=480)

# FIN
window.mainloop()
