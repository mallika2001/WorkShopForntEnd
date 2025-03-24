import tkinter as tk
from tkinter import ttk, messagebox

class CustomersPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.customers = [
            {"customer_id": 1, "name": "John Doe", "contact": "1234567890", "email": "john@example.com", "address": "123 Street, NY"},
            {"customer_id": 2, "name": "Jane Smith", "contact": "9876543210", "email": "jane@example.com", "address": "456 Avenue, LA"}
        ]

        self.selected_customer = None  # Track selected customer for editing

        # Heading
        tk.Label(self, text="Customer Management", font=("Arial", 16, "bold")).pack(pady=10)

        # Table Frame
        table_frame = tk.Frame(self)
        table_frame.pack(pady=10)

        self.tree = ttk.Treeview(table_frame, columns=("ID", "Name", "Contact", "Email", "Address"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Contact", text="Contact")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Name", width=150)
        self.tree.column("Contact", width=100, anchor="center")
        self.tree.column("Email", width=180)
        self.tree.column("Address", width=200)

        self.tree.bind("<<TreeviewSelect>>", self.select_customer)
        self.tree.pack()

        self.load_customers()

        # Form Frame
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Contact:").grid(row=1, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(form_frame, width=30)
        self.contact_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(form_frame, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(form_frame, width=30)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Customer", command=self.add_customer, bg="green", fg="white", width=15).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Update Customer", command=self.update_customer, bg="blue", fg="white", width=15).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Delete Customer", command=self.delete_customer, bg="red", fg="white", width=15).grid(row=0, column=2, padx=5)

    def load_customers(self):
        """ Load customers into the table """
        self.tree.delete(*self.tree.get_children())
        for customer in self.customers:
            self.tree.insert("", "end", values=(customer["customer_id"], customer["name"], customer["contact"], customer["email"], customer["address"]))

    def select_customer(self, event):
        """ Select a customer from the table and populate the form """
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            values = item["values"]
            self.selected_customer = values[0]  # Store selected customer ID

            # Fill form fields
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[1])

            self.contact_entry.delete(0, tk.END)
            self.contact_entry.insert(0, values[2])

            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, values[3])

            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, values[4])

    def add_customer(self):
        """ Add a new customer """
        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if not name or not contact or not email or not address:
            messagebox.showerror("Error", "All fields are required!")
            return

        new_id = max([c["customer_id"] for c in self.customers], default=0) + 1
        self.customers.append({"customer_id": new_id, "name": name, "contact": contact, "email": email, "address": address})
        self.load_customers()
        self.clear_form()
        messagebox.showinfo("Success", "Customer added successfully!")

    def update_customer(self):
        """ Update an existing customer """
        if self.selected_customer is None:
            messagebox.showerror("Error", "Please select a customer to update!")
            return

        name = self.name_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        for customer in self.customers:
            if customer["customer_id"] == self.selected_customer:
                customer["name"] = name
                customer["contact"] = contact
                customer["email"] = email
                customer["address"] = address
                break

        self.load_customers()
        self.clear_form()
        messagebox.showinfo("Success", "Customer updated successfully!")

    def delete_customer(self):
        """ Delete selected customer """
        if self.selected_customer is None:
            messagebox.showerror("Error", "Please select a customer to delete!")
            return

        self.customers = [c for c in self.customers if c["customer_id"] != self.selected_customer]
        self.load_customers()
        self.clear_form()
        messagebox.showinfo("Success", "Customer deleted successfully!")

    def clear_form(self):
        """ Clear the form fields """
        self.name_entry.delete(0, tk.END)
        self.contact_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.selected_customer = None

