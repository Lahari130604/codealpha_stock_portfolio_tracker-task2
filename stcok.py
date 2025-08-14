import tkinter as tk
from tkinter import messagebox, filedialog
import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}

# Function to calculate total investment
def calculate_investment():
    stock = stock_entry.get().upper()
    try:
        quantity = int(quantity_entry.get())
        if stock in stock_prices:
            price = stock_prices[stock]
            total = price * quantity
            result_label.config(text=f"💰 Total Investment: ${total}", fg="green")
            return stock, quantity, total
        else:
            messagebox.showerror("Error", "Stock not found in price list.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity.")

# Function to save result
def save_result():
    data = calculate_investment()
    if data:
        file_type = file_type_var.get()
        if file_type == "txt":
            with open("investment.txt", "w") as f:
                f.write(f"Stock: {data[0]}, Quantity: {data[1]}, Total: ${data[2]}")
        elif file_type == "csv":
            with open("investment.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Total"])
                writer.writerow([data[0], data[1], data[2]])
        messagebox.showinfo("Saved", f"Result saved as {file_type.upper()} file!")

# GUI setup
root = tk.Tk()
root.title("📊 Stock Portfolio Tracker")
root.geometry("400x300")
root.config(bg="#f0f8ff")

# Labels and Entries
tk.Label(root, text="Enter Stock Symbol:", bg="#f0f8ff", font=("Arial", 12)).pack(pady=5)
stock_entry = tk.Entry(root, font=("Arial", 12))
stock_entry.pack(pady=5)

tk.Label(root, text="Enter Quantity:", bg="#f0f8ff", font=("Arial", 12)).pack(pady=5)
quantity_entry = tk.Entry(root, font=("Arial", 12))
quantity_entry.pack(pady=5)

# File type selection
file_type_var = tk.StringVar(value="txt")
tk.Label(root, text="Save as:", bg="#f0f8ff", font=("Arial", 12)).pack(pady=5)
tk.Radiobutton(root, text="Text File (.txt)", variable=file_type_var, value="txt", bg="#f0f8ff").pack()
tk.Radiobutton(root, text="CSV File (.csv)", variable=file_type_var, value="csv", bg="#f0f8ff").pack()

# Buttons
tk.Button(root, text="Calculate", command=calculate_investment, bg="#add8e6", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Save Result", command=save_result, bg="#90ee90", font=("Arial", 12)).pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", bg="#f0f8ff", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
