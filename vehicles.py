import tkinter as tk
from tkinter import ttk, messagebox

class VehiclesPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")
        
        # Sample Data (Replace with Database later)
        self.vehicles = [
            {"ID": 1, "Customer": "John Doe", "Make": "Toyota", "Model": "Corolla", "Year": "2020", "VIN": "123ABC", "Plate": "XYZ-123"},
            {"ID": 2, "Customer": "Alice Smith", "Make": "Ford", "Model": "Mustang", "Year": "2019", "VIN": "456DEF", "Plate": "ABC-789"}
        ]

        # Header
        tk.Label(self, text="Vehicle Management", font=("Arial", 16, "bold"), bg="#ECF0F1").pack(pady=10)

        # Table
        self.tree = ttk.Treeview(self, columns=("ID", "Customer", "Make", "Model", "Year", "VIN", "Plate"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(pady=10, padx=20, fill="both", expand=True)
        self.load_data()

        # Form
        form_frame = tk.Frame(self, bg="#ECF0F1")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Customer:").grid(row=0, column=0)
        self.customer_entry = tk.Entry(form_frame)
        self.customer_entry.grid(row=0, column=1, padx=10)

        tk.Label(form_frame, text="Make:").grid(row=0, column=2)
        self.make_entry = tk.Entry(form_frame)
        self.make_entry.grid(row=0, column=3, padx=10)

        tk.Label(form_frame, text="Model:").grid(row=1, column=0)
        self.model_entry = tk.Entry(form_frame)
        self.model_entry.grid(row=1, column=1, padx=10)

        tk.Label(form_frame, text="Year:").grid(row=1, column=2)
        self.year_entry = tk.Entry(form_frame)
        self.year_entry.grid(row=1, column=3, padx=10)

        tk.Label(form_frame, text="VIN:").grid(row=2, column=0)
        self.vin_entry = tk.Entry(form_frame)
        self.vin_entry.grid(row=2, column=1, padx=10)

        tk.Label(form_frame, text="Plate:").grid(row=2, column=2)
        self.plate_entry = tk.Entry(form_frame)
        self.plate_entry.grid(row=2, column=3, padx=10)

        # Buttons
        button_frame = tk.Frame(self, bg="#ECF0F1")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Vehicle", bg="#27AE60", fg="white", command=self.add_vehicle).pack(side="left", padx=10)
        tk.Button(button_frame, text="Update Vehicle", bg="#F39C12", fg="white", command=self.update_vehicle).pack(side="left", padx=10)
        tk.Button(button_frame, text="Delete Vehicle", bg="#E74C3C", fg="white", command=self.delete_vehicle).pack(side="left", padx=10)

    def load_data(self):
        """ Load sample data into the table """
        for vehicle in self.vehicles:
            self.tree.insert("", "end", values=(vehicle["ID"], vehicle["Customer"], vehicle["Make"], vehicle["Model"], vehicle["Year"], vehicle["VIN"], vehicle["Plate"]))

    def add_vehicle(self):
        """ Add a new vehicle """
        new_id = len(self.vehicles) + 1
        new_vehicle = {
            "ID": new_id,
            "Customer": self.customer_entry.get(),
            "Make": self.make_entry.get(),
            "Model": self.model_entry.get(),
            "Year": self.year_entry.get(),
            "VIN": self.vin_entry.get(),
            "Plate": self.plate_entry.get()
        }
        self.vehicles.append(new_vehicle)
        self.tree.insert("", "end", values=(new_id, new_vehicle["Customer"], new_vehicle["Make"], new_vehicle["Model"], new_vehicle["Year"], new_vehicle["VIN"], new_vehicle["Plate"]))
        messagebox.showinfo("Success", "Vehicle added successfully!")
        self.clear_fields()

    def update_vehicle(self):
        """ Update selected vehicle """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a vehicle to update.")
            return

        item_index = self.tree.index(selected_item)
        updated_vehicle = {
            "ID": self.vehicles[item_index]["ID"],
            "Customer": self.customer_entry.get(),
            "Make": self.make_entry.get(),
            "Model": self.model_entry.get(),
            "Year": self.year_entry.get(),
            "VIN": self.vin_entry.get(),
            "Plate": self.plate_entry.get()
        }

        self.vehicles[item_index] = updated_vehicle
        self.tree.item(selected_item, values=(updated_vehicle["ID"], updated_vehicle["Customer"], updated_vehicle["Make"], updated_vehicle["Model"], updated_vehicle["Year"], updated_vehicle["VIN"], updated_vehicle["Plate"]))
        messagebox.showinfo("Success", "Vehicle updated successfully!")
        self.clear_fields()

    def delete_vehicle(self):
        """ Delete selected vehicle """
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a vehicle to delete.")
            return

        item_index = self.tree.index(selected_item)
        del self.vehicles[item_index]
        self.tree.delete(selected_item)
        messagebox.showinfo("Success", "Vehicle deleted successfully!")

    def clear_fields(self):
        """ Clear all input fields """
        self.customer_entry.delete(0, tk.END)
        self.make_entry.delete(0, tk.END)
        self.model_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.vin_entry.delete(0, tk.END)
        self.plate_entry.delete(0, tk.END)
