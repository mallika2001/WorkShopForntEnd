import tkinter as tk
from tkinter import ttk
 
def submit_customer():
    name = name_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    reg_date = reg_date_entry.get()
    
    print(f"Customer Registered: {name}, {contact}, {email}, {address}, {reg_date}")
 
# Create main window
root = tk.Tk()
root.title("Customer Registration")
root.geometry("400x300")
 
# Create frame
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
# Labels and Entry Fields
ttk.Label(frame, text="Full Name:").grid(row=0, column=0, sticky="w", pady=5)
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
 
ttk.Label(frame, text="Registration Date:").grid(row=4, column=0, sticky="w", pady=5)
reg_date_entry = ttk.Entry(frame, width=40)
reg_date_entry.grid(row=4, column=1, pady=5)
 
# Submit Button
submit_button = ttk.Button(frame, text="Submit", command=submit_customer)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)
 
# Run the application
root.mainloop()
 