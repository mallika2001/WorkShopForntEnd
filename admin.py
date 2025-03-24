import tkinter as tk
from orders import OrdersDashboard
from inventory import InventoryDashboard
from supplier import SupplierDashboard
from invoices import InvoiceDashboard
from feedback import FeedbackDashboard

class AdminDashboard:
    def __init__(self, parent):
        self.parent = parent

        tk.Label(parent, text="Admin Dashboard", font=("Arial", 16)).pack(pady=10)

        tk.Button(parent, text="Manage Orders", command=self.show_orders).pack(fill=tk.X, pady=5)
        tk.Button(parent, text="Manage Inventory", command=self.show_inventory).pack(fill=tk.X, pady=5)
        tk.Button(parent, text="Manage Suppliers", command=self.show_suppliers).pack(fill=tk.X, pady=5)
        tk.Button(parent, text="Invoices", command=self.show_invoices).pack(fill=tk.X, pady=5)
        tk.Button(parent, text="Customer Feedback", command=self.show_feedback).pack(fill=tk.X, pady=5)

        self.content_frame = tk.Frame(parent)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

    def show_orders(self):
        self.clear_frame()
        OrdersDashboard(self.content_frame)

    def show_inventory(self):
        self.clear_frame()
        InventoryDashboard(self.content_frame)

    def show_suppliers(self):
        self.clear_frame()
        SupplierDashboard(self.content_frame)

    def show_invoices(self):
        self.clear_frame()
        InvoiceDashboard(self.content_frame)

    def show_feedback(self):
        self.clear_frame()
        FeedbackDashboard(self.content_frame)

    def clear_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
