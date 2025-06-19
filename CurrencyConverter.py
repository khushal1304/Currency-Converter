import tkinter as tk
from tkinter import ttk, messagebox

# Currency rates example (You can update these with real-time rates)
currency_rates = {
    'USD': 1.0,
    'INR': 83.0,
    'EUR': 0.93,
    'GBP': 0.8,
    'JPY': 155.0
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()

        if from_curr not in currency_rates or to_curr not in currency_rates:
            messagebox.showerror("Error", "Invalid currency selected.")
            return

        usd_amount = amount / currency_rates[from_curr]
        converted_amount = usd_amount * currency_rates[to_curr]

        result_label.config(text=f"{amount} {from_curr} = {round(converted_amount, 2)} {to_curr}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# UI Setup
app = tk.Tk()
app.title("Currency Converter")
app.geometry("400x250")
app.resizable(False, False)

# Amount Entry
tk.Label(app, text="Amount:", font=("Arial", 12)).pack(pady=5)
amount_entry = tk.Entry(app, font=("Arial", 12))
amount_entry.pack()

# From Currency
tk.Label(app, text="From:", font=("Arial", 12)).pack(pady=5)
from_currency = ttk.Combobox(app, values=list(currency_rates.keys()), font=("Arial", 12))
from_currency.pack()
from_currency.set("USD")

# To Currency
tk.Label(app, text="To:", font=("Arial", 12)).pack(pady=5)
to_currency = ttk.Combobox(app, values=list(currency_rates.keys()), font=("Arial", 12))
to_currency.pack()
to_currency.set("INR")

# Convert Button
convert_button = tk.Button(app, text="Convert", command=convert_currency, font=("Arial", 12), bg="green", fg="white")
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(app, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

app.mainloop()