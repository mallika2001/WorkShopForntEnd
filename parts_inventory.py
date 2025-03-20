import tkinter as tk
from tkinter import ttk
 
def submit_part():
    part_name = part_name_entry.get()
    description = description_entry.get()
    stock = stock_entry.get()
    price = price_entry.get()
    supplier_id = supplier_id_entry.get()
    
    print(f"Part Added: {part_name}, {description}, {stock}, {price}, {supplier_id}")
 
root = tk.Tk()
root.title("Parts Inventory")
root.geometry("400x300")
 
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Part Name:").grid(row=0, column=0, sticky="w", pady=5)
part_name_entry = ttk.Entry(frame, width=40)
part_name_entry.grid(row=0, column=1, pady=5)
 
ttk.Label(frame, text="Description:").grid(row=1, column=0, sticky="w", pady=5)
description_entry = ttk.Entry(frame, width=40)
description_entry.grid(row=1, column=1, pady=5)
 
ttk.Label(frame, text="Stock Quantity:").grid(row=2, column=0, sticky="w", pady=5)
stock_entry = ttk.Entry(frame, width=40)
stock_entry.grid(row=2, column=1, pady=5)
 
ttk.Label(frame, text="Price per Unit:").grid(row=3, column=0, sticky="w", pady=5)
price_entry = ttk.Entry(frame, width=40)
price_entry.grid(row=3, column=1, pady=5)
 
ttk.Label(frame, text="Supplier ID:").grid(row=4, column=0, sticky="w", pady=5)
supplier_id_entry = ttk.Entry(frame, width=40)
supplier_id_entry.grid(row=4, column=1, pady=5)
 
submit_button = ttk.Button(frame, text="Submit", command=submit_part)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)
 
root.mainloop()