import tkinter as tk
from tkinter import ttk
 
def submit_supplier():
    name = name_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    print(f"Supplier Added: {name}, {contact}, {email}, {address}")
 
root = tk.Tk()
root.title("Supplier Management")
root.geometry("400x250")
 
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Supplier Name:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = ttk.Entry(frame, width=40)
name_entry.grid(row=0, column=1, pady=5)
 
ttk.Label(frame, text="Contact Number:").grid(row=1, column=0, sticky="w", pady=5)
contact_entry = ttk.Entry(frame, width=40)
contact_entry.grid(row=1, column=1, pady=5)
 
ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
email_entry = ttk.Entry(frame, width=40)
email_entry.grid(row=2, column=1, pady=5)
 
ttk.Label(frame, text="Address:").grid(row=3, column=0, sticky="w", pady=5)
address_entry = ttk.Entry(frame, width=40)
address_entry.grid(row=3, column=1, pady=5)
 
submit_button = ttk.Button(frame, text="Submit", command=submit_supplier)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)