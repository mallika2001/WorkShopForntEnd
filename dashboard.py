import tkinter as tk
from customers import CustomerDashboard
from orders import OrdersDashboard
from inventory import InventoryDashboard
from invoices import InvoiceDashboard
from feedback import FeedbackDashboard

class MainDashboard:
    def __init__(self, parent, role, controller):
        self.parent = parent
        self.controller = controller
        self.role = role
        
        tk.Label(parent, text=f"{role.capitalize()} Dashboard", font=("Arial", 18, "bold")).pack(pady=10)

        options = []
        
        if role == "admin":
            options = [
                ("Manage Customers", lambda: controller.load_module(CustomerDashboard)),
                ("Manage Orders", lambda: controller.load_module(OrdersDashboard)),
                ("Manage Inventory", lambda: controller.load_module(InventoryDashboard)),
                ("Manage Invoices", lambda: controller.load_module(InvoiceDashboard)),
                ("View Feedback", lambda: controller.load_module(FeedbackDashboard)),
            ]
        elif role == "mechanic":
            options = [
                ("View Assigned Work", lambda: controller.load_module(OrdersDashboard)),
                ("Update Work Status", lambda: controller.load_module(OrdersDashboard)),
            ]
        elif role == "customer":
            options = [
                ("View My Orders", lambda: controller.load_module(OrdersDashboard)),
                ("Give Feedback", lambda: controller.load_module(FeedbackDashboard)),
            ]

        for text, command in options:
            tk.Button(parent, text=text, command=command, font=("Arial", 12), width=30, height=2).pack(pady=5)
