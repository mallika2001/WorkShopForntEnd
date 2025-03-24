import tkinter as tk
from tkinter import messagebox

class CustomerDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Dashboard - Pharmacy Inventory")
        self.root.geometry("600x400")

        tk.Label(self.root, text="Customer Dashboard", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="View Medicines", width=20, command=self.view_medicines).pack(pady=5)
        tk.Button(self.root, text="Place Order", width=20, command=self.place_order).pack(pady=5)
        tk.Button(self.root, text="Order History", width=20, command=self.view_orders).pack(pady=5)
        tk.Button(self.root, text="Give Feedback", width=20, command=self.give_feedback).pack(pady=5)
        tk.Button(self.root, text="Logout", width=20, command=self.logout).pack(pady=20)

    def view_medicines(self):
        messagebox.showinfo("Medicines", "View Available Medicines Module")

    def place_order(self):
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "order_management.py", "customer"])  # Open Order Management as Customer


    def view_orders(self):
        messagebox.showinfo("Orders", "View Order History Module")

    def give_feedback(self):
        messagebox.showinfo("Feedback", "Provide Feedback Module")
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "feedback_system.py"])  # Open Feedback System
    def view_medicines(self):
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "view_medicines.py"])  # Open View Medicines
    def view_orders(self):
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "order_history.py"])  # Open Order History

    def logout(self):
        self.root.destroy()
        from phramaLogin import LoginApp
        root = tk.Tk()
        LoginApp(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomerDashboard(root)
    root.mainloop()
