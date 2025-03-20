import tkinter as tk
from tkinter import ttk
 
def submit_service():
    service_name = service_name_entry.get()
    description = description_entry.get()
    cost = cost_entry.get()
    duration = duration_entry.get()
    
    print(f"Service Added: {service_name}, {description}, {cost}, {duration}")
 
root = tk.Tk()
root.title("Modification Services")
root.geometry("400x250")
 
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Service Name:").grid(row=0, column=0, sticky="w", pady=5)
service_name_entry = ttk.Entry(frame, width=40)
service_name_entry.grid(row=0, column=1, pady=5)
 
ttk.Label(frame, text="Description:").grid(row=1, column=0, sticky="w", pady=5)
description_entry = ttk.Entry(frame, width=40)
description_entry.grid(row=1, column=1, pady=5)
 
ttk.Label(frame, text="Cost:").grid(row=2, column=0, sticky="w", pady=5)
cost_entry = ttk.Entry(frame, width=40)
cost_entry.grid(row=2, column=1, pady=5)
 
ttk.Label(frame, text="Duration:").grid(row=3, column=0, sticky="w", pady=5)
duration_entry = ttk.Entry(frame, width=40)
duration_entry.grid(row=3, column=1, pady=5)
 
submit_button = ttk.Button(frame, text="Submit", command=submit_service)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)
 
root.mainloop()