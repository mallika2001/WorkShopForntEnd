import tkinter as tk
from tkinter import ttk
 
def submit_vehicle():
    customer_id = customer_id_entry.get()
    make = make_entry.get()
    model = model_entry.get()
    year = year_entry.get()
    vin = vin_entry.get()
    license_plate = license_plate_entry.get()
    
    print(f"Vehicle Registered: {customer_id}, {make}, {model}, {year}, {vin}, {license_plate}")
 
root = tk.Tk()
root.title("Vehicle Registration")
root.geometry("400x300")
 
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Customer ID:").grid(row=0, column=0, sticky="w", pady=5)
customer_id_entry = ttk.Entry(frame, width=40)
customer_id_entry.grid(row=0, column=1, pady=5)
 
ttk.Label(frame, text="Make:").grid(row=1, column=0, sticky="w", pady=5)
make_entry = ttk.Entry(frame, width=40)
make_entry.grid(row=1, column=1, pady=5)
 
ttk.Label(frame, text="Model:").grid(row=2, column=0, sticky="w", pady=5)
model_entry = ttk.Entry(frame, width=40)
model_entry.grid(row=2, column=1, pady=5)
 
ttk.Label(frame, text="Year:").grid(row=3, column=0, sticky="w", pady=5)
year_entry = ttk.Entry(frame, width=40)
year_entry.grid(row=3, column=1, pady=5)
 
ttk.Label(frame, text="VIN Number:").grid(row=4, column=0, sticky="w", pady=5)
vin_entry = ttk.Entry(frame, width=40)
vin_entry.grid(row=4, column=1, pady=5)
 
ttk.Label(frame, text="License Plate:").grid(row=5, column=0, sticky="w", pady=5)
license_plate_entry = ttk.Entry(frame, width=40)
license_plate_entry.grid(row=5, column=1, pady=5)
 
submit_button = ttk.Button(frame, text="Submit", command=submit_vehicle)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)
 
root.mainloop()
 