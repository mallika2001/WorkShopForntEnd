import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class OrderHistory:
    def __init__(self, root):
        self.root = root
        self.root.title("Order History - Pharmacy Inventory")
        self.root.geometry("600x400")

        tk.Label(self.root, text="Your Order History", font=("Arial", 18)).pack(pady=10)

        # Order History Table
        self.tree = ttk.Treeview(self.root, columns=("Order ID", "Medicine", "Quantity", "Status"), show="headings")
        self.tree.heading("Order ID", text="Order ID")
        self.tree.heading("Medicine", text="Medicine")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Status", text="Status")
        self.tree.pack(pady=10)

        self.load_dummy_orders()

        # Back Button
        tk.Button(self.root, text="Back", width=15, command=self.go_back).pack(pady=10)

    def load_dummy_orders(self):
        data = [(1, "Paracetamol", 2, "Shipped"), (2, "Ibuprofen", 1, "Pending")]
        for item in data:
            self.tree.insert("", "end", values=item)

    def go_back(self):
        self.root.destroy()
        subprocess.run(["python", "customer_dashboard.py"])

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderHistory(root)
    root.mainloop()
