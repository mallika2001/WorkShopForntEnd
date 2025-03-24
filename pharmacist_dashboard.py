import tkinter as tk
from tkinter import messagebox

class PharmacistDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacist Dashboard - Pharmacy Inventory")
        self.root.geometry("600x400")

        tk.Label(self.root, text="Pharmacist Dashboard", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Manage Inventory", width=20, command=self.manage_inventory).pack(pady=5)
        tk.Button(self.root, text="View Orders", width=20, command=self.view_orders).pack(pady=5)
        tk.Button(self.root, text="Logout", width=20, command=self.logout).pack(pady=20)

    def manage_inventory(self):
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "inventory_management.py", "pharmacist"])



    def view_orders(self):
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "order_management.py", "pharmacist"])  # Open as Pharmacist

    def logout(self):
        self.root.destroy()
        from phramaLogin import LoginApp
        root = tk.Tk()
        LoginApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacistDashboard(root)
    root.mainloop()
