import tkinter as tk
from tkinter import ttk
 
def submit_invoice():
    order_id = order_id_entry.get()
    customer_id = customer_id_entry.get()
    total_amount = total_amount_entry.get()
    payment_status = payment_status_entry.get()
    payment_method = payment_method_entry.get()
    invoice_date = invoice_date_entry.get()
    
    print(f"Invoice Generated: {order_id}, {customer_id}, {total_amount}, {payment_status}, {payment_method}, {invoice_date}")
 
root = tk.Tk()
root.title("Invoices")
root.geometry("400x300")
 
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Order ID:").grid(row=0, column=0, sticky="w", pady=5)
order_id_entry = ttk.Entry(frame, width=40)
order_id_entry.grid(row=0, column=1, pady=5)
 
ttk.Label(frame, text="Customer ID:").grid(row=1, column=0, sticky="w", pady=5)
customer_id_entry = ttk.Entry(frame, width=40)
customer_id_entry.grid(row=1, column=1, pady=5)
 
ttk.Label(frame, text="Total Amount:").grid(row=2, column=0, sticky="w", pady=5)
total_amount_entry = ttk.Entry(frame, width=40)
total_amount_entry.grid(row=2, column=1, pady=5)
 
ttk.Label(frame, text="Payment Status (Pending/Paid):").grid(row=3, column=0, sticky="w", pady=5)
payment_status_entry = ttk.Entry(frame, width=40)
payment_status_entry.grid(row=3, column=1, pady=5)
 
ttk.Label(frame, text="Payment Method (Cash/Credit Card/Online):").grid(row=4, column=0, sticky="w", pady=5)
payment_method_entry = ttk.Entry(frame, width=40)
payment_method_entry.grid(row=4, column=1, pady=5)
 
ttk.Label(frame, text="Invoice Date:").grid(row=5, column=0, sticky="w", pady=5)
invoice_date_entry = ttk.Entry(frame, width=40)
invoice_date_entry.grid(row=5, column=1, pady=5)
 
submit_button = ttk.Button(frame, text="Submit", command=submit_invoice)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)
 
root.mainloop()