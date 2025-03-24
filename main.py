import tkinter as tk
from customer import CustomersPage
from vehicles import VehiclesPage
from orders import OrdersPage
from staff import StaffPage
from parts import PartsPage
from invoices import InvoicesPage
from feedback import FeedbackPage
from supplier import SuppliersPage

class MainApp(tk.Tk):
    def __init__(self, role):
        super().__init__()
        self.title(f"{role} Dashboard")
        self.geometry("1000x600")
        self.role = role

        # Sidebar
        self.sidebar = tk.Frame(self, width=200, bg="#2C3E50")
        self.sidebar.pack(side="left", fill="y")

        # Content Area
        self.content_frame = tk.Frame(self, bg="#ECF0F1")
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.build_sidebar()

    def build_sidebar(self):
        tk.Label(self.sidebar, text=f"{self.role} Menu", fg="white", bg="#2C3E50", font=("Arial", 14, "bold")).pack(pady=15)

        def add_button(label, command):
            tk.Button(self.sidebar, text=label, command=command, bg="#34495E", fg="white", width=20).pack(pady=5)

        if self.role == "Admin":
            add_button("Customers", lambda: self.show(CustomersPage))
            add_button("Vehicles", lambda: self.show(VehiclesPage))
            add_button("Orders", lambda: self.show(OrdersPage))
            add_button("Staff", lambda: self.show(StaffPage))
            add_button("Parts", lambda: self.show(PartsPage))
            add_button("Invoices", lambda: self.show(InvoicesPage))
            add_button("Feedback", lambda: self.show(FeedbackPage))
            add_button("Suppliers", lambda: self.show(SuppliersPage))

        elif self.role == "Mechanic":
            add_button("Orders", lambda: self.show(OrdersPage))
            add_button("Feedback", lambda: self.show(FeedbackPage))

        elif self.role == "Customer":
            add_button("My Orders", lambda: self.show(OrdersPage))
            add_button("Give Feedback", lambda: self.show(FeedbackPage))

        tk.Button(self.sidebar, text="Logout", command=self.destroy, bg="#E74C3C", fg="white", width=20).pack(pady=20)

    def show(self, page_class):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        page_class(self.content_frame).pack(fill="both", expand=True)

if __name__ == "__main__":
    MainApp("Admin").mainloop()  # For testing without login
