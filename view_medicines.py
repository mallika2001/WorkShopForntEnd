import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class ViewMedicines:
    def __init__(self, root):
        self.root = root
        self.root.title("Available Medicines - Pharmacy Inventory")
        self.root.geometry("600x400")

        tk.Label(self.root, text="Available Medicines", font=("Arial", 18)).pack(pady=10)

        # Medicine List Table
        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Price"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Medicine Name")
        self.tree.heading("Price", text="Price ($)")
        self.tree.pack(pady=10)

        self.load_dummy_data()

        # Back Button
        tk.Button(self.root, text="Back", width=15, command=self.go_back).pack(pady=10)

    def load_dummy_data(self):
        data = [(1, "Paracetamol", 5), (2, "Aspirin", 3), (3, "Ibuprofen", 8)]
        for item in data:
            self.tree.insert("", "end", values=item)

    def go_back(self):
        self.root.destroy()
        subprocess.run(["python", "customer_dashboard.py"])

if __name__ == "__main__":
    root = tk.Tk()
    app = ViewMedicines(root)
    root.mainloop()
