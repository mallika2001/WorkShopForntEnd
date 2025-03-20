import tkinter as tk
from tkinter import ttk
import subprocess
 
def open_module(module_name):
    try:
        subprocess.Popen(["python3", module_name])  # Explicitly use python3
    except Exception as e:
        print(f"Error opening {module_name}: {e}")
 
root = tk.Tk()
root.title("Workshop Management Dashboard")
root.geometry("400x500")
 
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Vehicle Modification Workshop", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
 
modules = [
    ("Customers", "customers.py"),
    ("Vehicles", "vehicles.py"),
    ("Modification Services", "modification_services.py"),
    ("Parts Inventory", "parts_inventory.py"),
    ("Suppliers", "suppliers.py"),
    ("Modification Orders", "modification_orders.py"),
    ("Staff", "staff.py"),
    ("Work Assignments", "work_assignments.py"),
    ("Invoices", "invoices.py"),
    ("Feedback & Reviews", "feedback_reviews.py"),
]
 
# Generate buttons for each module
for i, (module_name, file_name) in enumerate(modules):
    ttk.Button(frame, text=module_name, width=30, command=lambda f=file_name: open_module(f)).grid(row=i+1, column=0, pady=5)
 
root.mainloop()
 