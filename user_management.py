import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class UserManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("User Management - Pharmacy Inventory")
        self.root.geometry("700x400")

        tk.Label(self.root, text="Manage Users", font=("Arial", 18)).pack(pady=10)

        # User List Table
        self.tree = ttk.Treeview(self.root, columns=("ID", "Username", "Role"), show="headings")
        self.tree.heading("ID", text="User ID")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Role", text="Role")
        self.tree.pack(pady=10)

        # Entry Fields
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        tk.Label(self.root, text="Role (pharmacist/customer):").pack()
        self.role_entry = tk.Entry(self.root)
        self.role_entry.pack()

        # Buttons
        tk.Button(self.root, text="Add User", width=15, command=self.add_user).pack(pady=5)
        tk.Button(self.root, text="Update Selected", width=15, command=self.update_user).pack(pady=5)
        tk.Button(self.root, text="Delete Selected", width=15, command=self.delete_user).pack(pady=5)
        tk.Button(self.root, text="Back", width=15, command=self.go_back).pack(pady=10)

        self.load_dummy_users()

    def go_back(self):
        self.root.destroy()
        subprocess.run(["python", "admin_dashboard.py"])

    def load_dummy_users(self):
        # Dummy data (Replace with database logic)
        data = [(1, "pharma1", "pharmacist"), (2, "cust1", "customer")]
        for item in data:
            self.tree.insert("", "end", values=item)

    def add_user(self):
        username = self.username_entry.get()
        role = self.role_entry.get()

        if username and role in ["pharmacist", "customer"]:
            new_id = len(self.tree.get_children()) + 1
            self.tree.insert("", "end", values=(new_id, username, role))
            messagebox.showinfo("Success", "User added successfully!")
        else:
            messagebox.showerror("Error", "Invalid username or role!")

    def update_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a user to update")
            return

        username = self.username_entry.get()
        role = self.role_entry.get()

        if username and role:
            self.tree.item(selected_item, values=(self.tree.item(selected_item)["values"][0], username, role))
            messagebox.showinfo("Success", "User updated successfully!")
        else:
            messagebox.showerror("Error", "All fields are required")

    def delete_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Select a user to delete")
            return

        self.tree.delete(selected_item)
        messagebox.showinfo("Success", "User deleted successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagement(root)
    root.mainloop()
