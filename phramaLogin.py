import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk, messagebox
import subprocess

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Inventory - Login")
        self.root.geometry("400x350")

        self.create_widgets()
        
    def apply_theme(root):
        style = ttk.Style()
        style.theme_use("clam")  # Use modern theme (clam, alt, default, classic)
        
        # Button Styling
        style.configure("TButton", font=("Arial", 12), padding=6, background="#2E86C1", foreground="white")
        
        # Label Styling
        style.configure("TLabel", font=("Arial", 12), padding=5)
        
        # Table (Treeview) Styling
        style.configure("Treeview", font=("Arial", 11), rowheight=25)
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

        root.configure(bg="#ECF0F1")  # Light background
    def create_widgets(self):
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.open_register_window).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin123":
            messagebox.showinfo("Login Success", "Welcome, Admin!")
            self.root.destroy()  # Close the login window
            subprocess.run(["python", "admin_dashboard.py"])  # Open admin dashboard

        elif username == "pharmacist" and password == "pharma123":
            messagebox.showinfo("Login Success", "Welcome, Pharmacist!")
            self.root.destroy()
            subprocess.run(["python", "pharmacist_dashboard.py"])  # Open Pharmacist Dashboard
        elif username == "customer" and password == "cust123":
            messagebox.showinfo("Login Success", "Welcome, Customer!")
            self.root.destroy()
            subprocess.run(["python", "customer_dashboard.py"])  # Open Customer Dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def open_register_window(self):
        reg_window = tk.Toplevel(self.root)
        reg_window.title("Register")
        reg_window.geometry("400x300")

        tk.Label(reg_window, text="Register", font=("Arial", 16)).pack(pady=10)

        tk.Label(reg_window, text="Username:").pack()
        username_entry = tk.Entry(reg_window)
        username_entry.pack()

        tk.Label(reg_window, text="Password:").pack()
        password_entry = tk.Entry(reg_window, show="*")
        password_entry.pack()

        tk.Button(reg_window, text="Register", command=lambda: self.register(username_entry.get(), password_entry.get())).pack(pady=10)

    def register(self, username, password):
        if username and password:
            messagebox.showinfo("Registration Success", "User registered successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
