import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class InventoryManagement:
    def __init__(self, root, user_role):
        self.root = root
        self.root.title("Inventory Management - Pharmacy Inventory")
        self.root.geometry("700x400")
        self.user_role = user_role  # Store user role

        tk.Label(self.root, text="Inventory Management", font=("Arial", 18)).pack(pady=10)

        # Medicine List Table
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Quantity", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Medicine Name")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.heading("Price", text="Price ($)")
        self.tree.pack(pady=10)

        # Entry Fields
        tk.Label(self.root, text="Medicine Name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Quantity:").pack()
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.pack()

        tk.Label(self.root, text="Price:").pack()
        self.price_entry = tk.Entry(self.root)
        self.price_entry.pack()

        # Buttons
        tk.Button(self.root, text="Add Medicine", width=15, command=self.add_medicine).pack(pady=5)
        tk.Button(self.root, text="Update Selected", width=15, command=self.update_medicine).pack(pady=5)
        tk.Button(self.root, text="Delete Selected", width=15, command=self.delete_medicine).pack(pady=5)
        tk.Button(self.root, text="Back", width=15, command=self.go_back).pack(pady=10)  # Back button

        self.load_dummy_data()

    def go_back(self):
        self.root.destroy()
        if self.user_role == "admin":
            subprocess.run(["python", "admin_dashboard.py"])
        else:
            subprocess.run(["python", "pharmacist_dashboard.py"])

    def load_dummy_data(self):
        data = [(1, "Paracetamol", 100, 5), (2, "Aspirin", 50, 3), (3, "Ibuprofen", 70, 8)]
        for item in data:
            self.tree.insert("", "end", values=item)

    def add_medicine(self):
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if name and quantity and price:
            new_id = len(self.tree.get_children()) + 1
            self.tree.insert("", "end", values=(new_id, name, quantity, price))
            messagebox.showinfo("Success", "Medicine added successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

    def update_medicine(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a medicine to update")
            return

        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        if name and quantity and price:
            self.tree.item(selected_item, values=(self.tree.item(selected_item)["values"][0], name, quantity, price))
            messagebox.showinfo("Success", "Medicine updated successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

    def delete_medicine(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a medicine to delete")
            return
        self.tree.delete(selected_item)
        messagebox.showinfo("Success", "Medicine deleted successfully!")

if __name__ == "__main__":
    import sys
    user_role = sys.argv[1] if len(sys.argv) > 1 else "admin"  # Default to admin
    root = tk.Tk()
    app = InventoryManagement(root, user_role)
    root.mainloop()
