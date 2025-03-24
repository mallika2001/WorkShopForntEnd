import tkinter as tk
from tkinter import messagebox

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard - Pharmacy Inventory")
        self.root.geometry("600x400")

        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Manage Inventory", width=20, command=self.manage_inventory).pack(pady=5)
        tk.Button(self.root, text="Manage Users", width=20, command=self.manage_users).pack(pady=5)
        tk.Button(self.root, text="View Orders", width=20, command=self.view_orders).pack(pady=5)
        tk.Button(self.root, text="Logout", width=20, command=self.logout).pack(pady=20)

    def manage_inventory(self):
        messagebox.showinfo("Inventory", "Manage Inventory Module")
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "inventory_management.py", "admin"])  # Open as Admin

    def manage_users(self):
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "user_management.py"])  # Open User Management


    def view_orders(self):
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "order_management.py", "admin"])  # Open Order Management as Admin


    def logout(self):
        self.root.destroy()
        from phramaLogin import LoginApp  # Redirect to login page
        root = tk.Tk()
        LoginApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()