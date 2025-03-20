import tkinter as tk
from tkinter import ttk
 
def submit_order():
    customer_id = customer_id_entry.get()
    vehicle_id = vehicle_id_entry.get()
    service_id = service_id_entry.get()
    total_cost = total_cost_entry.get()
    order_date = order_date_entry.get()
    status = status_entry.get()
    
    print(f"Order Placed: {customer_id}, {vehicle_id}, {service_id}, {total_cost}, {order_date}, {status}")
 
root = tk.Tk()
root.title("Modification Orders")
root.geometry("400x300")
 
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Customer ID:").grid(row=0, column=0, sticky="w", pady=5)
customer_id_entry = ttk.Entry(frame, width=40)
customer_id_entry.grid(row=0, column=1, pady=5)
 
ttk.Label(frame, text="Vehicle ID:").grid(row=1, column=0, sticky="w", pady=5)
vehicle_id_entry = ttk.Entry(frame, width=40)
vehicle_id_entry.grid(row=1, column=1, pady=5)
 
ttk.Label(frame, text="Service ID:").grid(row=2, column=0, sticky="w", pady=5)
service_id_entry = ttk.Entry(frame, width=40)
service_id_entry.grid(row=2, column=1, pady=5)
 
ttk.Label(frame, text="Total Cost:").grid(row=3, column=0, sticky="w", pady=5)
total_cost_entry = ttk.Entry(frame, width=40)
total_cost_entry.grid(row=3, column=1, pady=5)
 
ttk.Label(frame, text="Order Date:").grid(row=4, column=0, sticky="w", pady=5)
order_date_entry = ttk.Entry(frame, width=40)
order_date_entry.grid(row=4, column=1, pady=5)
 
ttk.Label(frame, text="Status (Pending/In Progress/Completed):").grid(row=5, column=0, sticky="w", pady=5)
status_entry = ttk.Entry(frame, width=40)
status_entry.grid(row=5, column=1, pady=5)
 
submit_button = ttk.Button(frame, text="Submit", command=submit_order)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)