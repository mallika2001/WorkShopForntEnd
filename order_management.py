import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys

class OrderManagement:
    def __init__(self, root, user_role="customer"):
        self.root = root
        self.root.title("Order Management - Pharmacy Inventory")
        self.root.geometry("700x400")
        self.user_role = user_role  # Store user role

        tk.Label(self.root, text="Order Management", font=("Arial", 18)).pack(pady=10)

        # Order Table
        self.tree = ttk.Treeview(self.root, columns=("Order ID", "Customer", "Medicine", "Quantity", "Status"), show="headings")
        self.tree.heading("Order ID", text="Order ID")
        self.tree.heading("Customer", text="Customer Name")
        self.tree.heading("Medicine", text="Medicine")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Status", text="Status")
        self.tree.pack(pady=10)

        # Admin & Pharmacist Controls
        if self.user_role in ["admin", "pharmacist"]:
            tk.Button(self.root, text="Mark as Processed", width=20, command=self.process_order).pack(pady=5)
            tk.Button(self.root, text="Delete Order", width=20, command=self.delete_order).pack(pady=5)

        # Back Button
        tk.Button(self.root, text="Back", width=15, command=self.go_back).pack(pady=10)

        self.load_dummy_orders()

    def load_dummy_orders(self):
        data = [(1, "John Doe", "Paracetamol", 2, "Pending"), (2, "Jane Smith", "Aspirin", 1, "Shipped")]
        for item in data:
            self.tree.insert("", "end", values=item)

    def process_order(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select an order to process")
            return
        values = self.tree.item(selected_item)["values"]
        self.tree.item(selected_item, values=(values[0], values[1], values[2], values[3], "Processed"))
        messagebox.showinfo("Success", "Order marked as processed!")

    def delete_order(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select an order to delete")
            return
        self.tree.delete(selected_item)
        messagebox.showinfo("Success", "Order deleted successfully!")

    def go_back(self):
        self.root.destroy()
        if self.user_role == "admin":
            subprocess.run(["python", "admin_dashboard.py"])
        elif self.user_role == "pharmacist":
            subprocess.run(["python", "pharmacist_dashboard.py"])
        else:
            subprocess.run(["python", "customer_dashboard.py"])

if __name__ == "__main__":
    user_role = sys.argv[1] if len(sys.argv) > 1 else "customer"
    root = tk.Tk()
    app = OrderManagement(root, user_role)
    root.mainloop()
