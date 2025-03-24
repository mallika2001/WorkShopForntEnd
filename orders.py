import tkinter as tk
from tkinter import ttk, messagebox

class OrdersPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")

        # Sample Data (Replace with Database later)
        self.orders = [
            {"ID": 1, "Customer": "John Doe", "Vehicle": "Toyota Corolla", "Service": "Engine Tuning", "Cost": "$500", "Date": "2024-03-10", "Status": "Completed"},
            {"ID": 2, "Customer": "Alice Smith", "Vehicle": "Ford Mustang", "Service": "Suspension Upgrade", "Cost": "$700", "Date": "2024-03-12", "Status": "Pending"}
        ]

        # Header
        tk.Label(self, text="Modification Orders Management", font=("Arial", 16, "bold"), bg="#ECF0F1").pack(pady=10)

        # Table
        self.tree = ttk.Treeview(self, columns=("ID", "Customer", "Vehicle", "Service", "Cost", "Date", "Status"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(pady=10, padx=20, fill="both", expand=True)
        self.load_data()

        # Form
        form_frame = tk.Frame(self, bg="#ECF0F1")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Customer:").grid(row=0, column=0)
        self.customer_entry = tk.Entry(form_frame)
        self.customer_entry.grid(row=0, column=1, padx=10)

        tk.Label(form_frame, text="Vehicle:").grid(row=0, column=2)
        self.vehicle_entry = tk.Entry(form_frame)
        self.vehicle_entry.grid(row=0, column=3, padx=10)

        tk.Label(form_frame, text="Service:").grid(row=1, column=0)
        self.service_entry = tk.Entry(form_frame)
        self.service_entry.grid(row=1, column=1, padx=10)

        tk.Label(form_frame, text="Cost:").grid(row=1, column=2)
        self.cost_entry = tk.Entry(form_frame)
        self.cost_entry.grid(row=1, column=3, padx=10)

        tk.Label(form_frame, text="Date:").grid(row=2, column=0)
        self.date_entry = tk.Entry(form_frame)
        self.date_entry.grid(row=2, column=1, padx=10)

        tk.Label(form_frame, text="Status:").grid(row=2, column=2)
        self.status_entry = tk.Entry(form_frame)
        self.status_entry.grid(row=2, column=3, padx=10)

        # Buttons
        button_frame = tk.Frame(self, bg="#ECF0F1")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Order", bg="#27AE60", fg="white", command=self.add_order).pack(side="left", padx=10)
        tk.Button(button_frame, text="Update Order", bg="#F39C12", fg="white", command=self.update_order).pack(side="left", padx=10)
        tk.Button(button_frame, text="Delete Order", bg="#E74C3C", fg="white", command=self.delete_order).pack(side="left", padx=10)

    def load_data(self):
        """ Load sample data into the table """
        for order in self.orders:
            self.tree.insert("", "end", values=(order["ID"], order["Customer"], order["Vehicle"], order["Service"], order["Cost"], order["Date"], order["Status"]))

    def add_order(self):
        """ Add a new order """
        new_id = len(self.orders) + 1
        new_order = {
            "ID": new_id,
            "Customer": self.customer_entry.get(),
            "Vehicle": self.vehicle_entry.get(),
            "Service": self.service_entry.get(),
            "Cost": self.cost_entry.get(),
            "Date": self.date_entry.get(),
            "Status": self.status_entry.get()
        }
        self.orders.append(new_order)
        self.tree.insert("", "end", values=(new_id, new_order["Customer"], new_order["Vehicle"], new_order["Service"], new_order["Cost"], new_order["Date"], new_order["Status"]))
        messagebox.showinfo("Success", "Order added successfully!")
        self.clear_fields()

    def update_order(self):
        """ Update selected order """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an order to update.")
            return

        item_index = self.tree.index(selected_item)
        updated_order = {
            "ID": self.orders[item_index]["ID"],
            "Customer": self.customer_entry.get(),
            "Vehicle": self.vehicle_entry.get(),
            "Service": self.service_entry.get(),
            "Cost": self.cost_entry.get(),
            "Date": self.date_entry.get(),
            "Status": self.status_entry.get()
        }

        self.orders[item_index] = updated_order
        self.tree.item(selected_item, values=(updated_order["ID"], updated_order["Customer"], updated_order["Vehicle"], updated_order["Service"], updated_order["Cost"], updated_order["Date"], updated_order["Status"]))
        messagebox.showinfo("Success", "Order updated successfully!")
        self.clear_fields()

    def delete_order(self):
        """ Delete selected order """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select an order to delete.")
            return

        item_index = self.tree.index(selected_item)
        del self.orders[item_index]
        self.tree.delete(selected_item)
        messagebox.showinfo("Success", "Order deleted successfully!")

    def clear_fields(self):
        """ Clear all input fields """
        self.customer_entry.delete(0, tk.END)
        self.vehicle_entry.delete(0, tk.END)
        self.service_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)
