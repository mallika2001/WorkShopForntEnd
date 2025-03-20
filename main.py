import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
 
# Function to load module content within the same page
def load_module_content(module_name):
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    ttk.Label(content_frame, text=f"{module_name}", font=("Arial", 16, "bold")).pack(pady=10)
    ttk.Label(content_frame, text=f"Content for {module_name} will be displayed here.").pack()
 
def show_dashboard(user_type):
    """Displays a dashboard with modules within the same window."""
    login_win.destroy()
 
    dashboard = tk.Tk()
    dashboard.title(f"{user_type} Dashboard")
    dashboard.geometry("800x500")
 
    # Sidebar Frame
    sidebar = tk.Frame(dashboard, width=200, bg="#2C3E50")
    sidebar.pack(side="left", fill="y")
 
    # Content Frame
    global content_frame
    content_frame = tk.Frame(dashboard)
    content_frame.pack(side="right", expand=True, fill="both")
 
    ttk.Label(content_frame, text=f"Welcome, {user_type}!", font=("Arial", 16, "bold")).pack(pady=10)
 
    # Define available functionalities
    if user_type == "Admin":
        modules = ["Customers", "Vehicles", "Modification Services",
                   "Parts Inventory", "Suppliers", "Modification Orders",
                   "Staff", "Work Assignments", "Invoices", "Feedback & Reviews"]
    elif user_type == "Mechanic":
        modules = ["Work Assignments", "Modification Orders"]
    else:  # Customer
        modules = ["Place Modification Order", "View Invoices", "Submit Feedback"]
 
    # Create module buttons in sidebar
    for module in modules:
        button = tk.Button(sidebar, text=module, width=25, height=2,
                           command=lambda m=module: load_module_content(m))
        button.pack(pady=5)
 
    dashboard.mainloop()
 
def register_customer():
    """Registers a new customer."""
    def save_customer():
        name = entry_name.get()
        contact = entry_contact.get()
        email = entry_email.get()
        address = entry_address.get()
 
        if not name or not contact:
            messagebox.showerror("Error", "Name and Contact are required!")
            return
 
        conn = sqlite3.connect("workshop.db")
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO customers (name, contact_number, email, address, registration_date) VALUES (?, ?, ?, ?, DATE('now'))",
                           (name, contact, email, address))
            conn.commit()
            messagebox.showinfo("Success", "Customer registered successfully!")
            reg_win.destroy()
            show_dashboard("Customer")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Contact or Email already exists!")
        finally:
            conn.close()
 
    reg_win = tk.Toplevel(login_win)
    reg_win.title("Register Customer")
    reg_win.geometry("300x300")
 
    ttk.Label(reg_win, text="Customer Registration", font=("Arial", 12, "bold")).pack(pady=10)
    ttk.Label(reg_win, text="Name:").pack()
    entry_name = ttk.Entry(reg_win)
    entry_name.pack()
 
    ttk.Label(reg_win, text="Contact Number:").pack()
    entry_contact = ttk.Entry(reg_win)
    entry_contact.pack()
 
    ttk.Label(reg_win, text="Email:").pack()
    entry_email = ttk.Entry(reg_win)
    entry_email.pack()
 
    ttk.Label(reg_win, text="Address:").pack()
    entry_address = ttk.Entry(reg_win)
    entry_address.pack()
 
    ttk.Button(reg_win, text="Register", command=save_customer).pack(pady=10)
 
def login_customer():
    """Checks if customer exists and opens customer dashboard or asks to register."""
    contact = entry_customer_contact.get()
 
    if not contact:
        messagebox.showerror("Error", "Please enter contact number!")
        return
 
    conn = sqlite3.connect("workshop.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers WHERE contact_number = ?", (contact,))
    customer = cursor.fetchone()
    conn.close()
 
    if customer:
        messagebox.showinfo("Welcome", f"Hello, {customer[1]}!")
        show_dashboard("Customer")
    else:
        if messagebox.askyesno("Not Found", "No customer found. Register?"):
            register_customer()
 
def login_admin():
    """Simple admin login."""
    password = entry_admin_password.get()
    if password == "admin123":  # Change this password if needed
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        show_dashboard("Admin")
    else:
        messagebox.showerror("Error", "Incorrect password!")
 
# GUI Setup
login_win = tk.Tk()
login_win.title("Workshop Management System - Login")
login_win.geometry("400x350")
 
frame = ttk.Frame(login_win, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Login as:", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
 
# Admin Login
ttk.Label(frame, text="Admin Password:").grid(row=1, column=0, pady=5)
entry_admin_password = ttk.Entry(frame, show="*")
entry_admin_password.grid(row=1, column=1, pady=5)
ttk.Button(frame, text="Login as Admin", command=login_admin).grid(row=2, column=0, columnspan=2, pady=5)
 
# Customer Login
ttk.Label(frame, text="Customer Contact:").grid(row=3, column=0, pady=5)
entry_customer_contact = ttk.Entry(frame)
entry_customer_contact.grid(row=3, column=1, pady=5)
ttk.Button(frame, text="Login as Customer", command=login_customer).grid(row=4, column=0, columnspan=2, pady=5)
 
# New Customer Registration
ttk.Button(frame, text="New Customer? Register Here", command=register_customer).grid(row=5, column=0, columnspan=2, pady=10)
 
login_win.mainloop()