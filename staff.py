import tkinter as tk
from tkinter import ttk
 
def submit_staff():
    name = name_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    role = role_entry.get()
    salary = salary_entry.get()
    
    print(f"Staff Added: {name}, {contact}, {email}, {role}, {salary}")
 
root = tk.Tk()
root.title("Staff Management")
root.geometry("400x300")
 
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Full Name:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = ttk.Entry(frame, width=40)
name_entry.grid(row=0, column=1, pady=5)
 
ttk.Label(frame, text="Contact Number:").grid(row=1, column=0, sticky="w", pady=5)
contact_entry = ttk.Entry(frame, width=40)
contact_entry.grid(row=1, column=1, pady=5)
 
ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
email_entry = ttk.Entry(frame, width=40)
email_entry.grid(row=2, column=1, pady=5)
 
ttk.Label(frame, text="Role:").grid(row=3, column=0, sticky="w", pady=5)
role_entry = ttk.Entry(frame, width=40)
role_entry.grid(row=3, column=1, pady=5)
 
ttk.Label(frame, text="Salary:").grid(row=4, column=0, sticky="w", pady=5)
salary_entry = ttk.Entry(frame, width=40)
salary_entry.grid(row=4, column=1, pady=5)
 
submit_button = ttk.Button(frame, text="Submit", command=submit_staff)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)
 
root.mainloop()