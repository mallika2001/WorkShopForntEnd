import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Sample data for users and roles
users_data = [
    {"username": "admin1", "role": "Admin"},
    {"username": "user1", "role": "User"},
    {"username": "user2", "role": "User"}
]

# Function to handle login
def login():
    username = login_username_entry.get()
    password = login_password_entry.get()
    role = login_role.get()
    
    if role == "Admin":
        # Add your admin login logic here
        messagebox.showinfo("Login", f"Admin logged in as {username}")
        open_admin_dashboard()
    elif role == "User":
        # Add your user login logic here
        messagebox.showinfo("Login", f"User logged in as {username}")
    else:
        messagebox.showerror("Error", "Please select a role")

# Function to handle registration
def register():
    username = register_username_entry.get()
    password = register_password_entry.get()
    confirm_password = register_confirm_password_entry.get()
    email = register_email_entry.get()
    phone = register_phone_entry.get()
    
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        # Add your registration logic here
        # For now, we'll just show a message and navigate to the login tab
        messagebox.showinfo("Register", f"Registered {username}")
        notebook.select(login_frame)

# Function to open admin dashboard
def open_admin_dashboard():
    admin_dashboard = tk.Toplevel(root)
    admin_dashboard.title("Admin Dashboard")
    
    ttk.Label(admin_dashboard, text="Welcome to the Admin Dashboard").pack(pady=10)
    
    ttk.Button(admin_dashboard, text="Manage Customers").pack(pady=5)
    ttk.Button(admin_dashboard, text="Manage Vehicles").pack(pady=5)
    ttk.Button(admin_dashboard, text="Manage Services").pack(pady=5)
    ttk.Button(admin_dashboard, text="Manage Parts Inventory").pack(pady=5)
    ttk.Button(admin_dashboard, text="Manage Suppliers").pack(pady=5)
    ttk.Button(admin_dashboard, text="Manage Orders").pack(pady=5)
    ttk.Button(admin_dashboard, text="Manage Staff").pack(pady=5)
    ttk.Button(admin_dashboard, text="View Invoices").pack(pady=5)
    ttk.Button(admin_dashboard, text="View Feedback & Reviews").pack(pady=5)
    ttk.Button(admin_dashboard, text="Manage User Roles", command=open_user_role_management).pack(pady=5)
    ttk.Button(admin_dashboard, text="View Users and Roles", command=view_users_and_roles).pack(pady=5)
    
    logout_button = ttk.Button(admin_dashboard, text="Logout", command=lambda: logout(admin_dashboard))
    logout_button.pack(pady=10)

# Function to handle logout
def logout(dashboard):
    dashboard.destroy()
    messagebox.showinfo("Logout", "You have been logged out")

# Function to open user role management window
def open_user_role_management():
    user_role_management = tk.Toplevel(root)
    user_role_management.title("User Role Management")
    
    ttk.Label(user_role_management, text="Manage User Roles").pack(pady=10)
    
    ttk.Label(user_role_management, text="Username").pack(pady=5)
    username_entry = ttk.Entry(user_role_management)
    username_entry.pack(pady=5)
    
    ttk.Label(user_role_management, text="Role").pack(pady=5)
    role_combobox = ttk.Combobox(user_role_management, values=["Admin", "User"])
    role_combobox.pack(pady=5)
    
    assign_role_button = ttk.Button(user_role_management, text="Assign Role", command=lambda: assign_role(username_entry.get(), role_combobox.get()))
    assign_role_button.pack(pady=10)
    
    ttk.Label(user_role_management, text="Search User").pack(pady=10)
    search_entry = ttk.Entry(user_role_management)
    search_entry.pack(pady=5)
    
    search_button = ttk.Button(user_role_management, text="Search", command=lambda: search_user(search_entry.get(), user_role_management))
    search_button.pack(pady=5)

# Function to assign role to a user
def assign_role(username, role):
    # Add your role assignment logic here
    for user in users_data:
        if user["username"] == username:
            user["role"] = role
            messagebox.showinfo("Role Assignment", f"Assigned role {role} to user {username}")
            return
    messagebox.showerror("Error", f"User {username} not found")

# Function to search for a user
def search_user(username, parent_window):
    for user in users_data:
        if user["username"] == username:
            edit_user_role(user, parent_window)
            return
    messagebox.showerror("Error", f"User {username} not found")

# Function to edit user role
def edit_user_role(user, parent_window):
    edit_window = tk.Toplevel(parent_window)
    edit_window.title("Edit User Role")
    
    ttk.Label(edit_window, text=f"Editing role for {user['username']}").pack(pady=10)
    
    ttk.Label(edit_window, text="Role").pack(pady=5)
    role_combobox = ttk.Combobox(edit_window, values=["Admin", "User"])
    role_combobox.set(user["role"])
    role_combobox.pack(pady=5)
    
    save_button = ttk.Button(edit_window, text="Save", command=lambda: save_role(user, role_combobox.get(), edit_window))
    save_button.pack(pady=10)

# Function to save the edited role
def save_role(user, new_role, edit_window):
    user["role"] = new_role
    messagebox.showinfo("Role Update", f"Updated role for {user['username']} to {new_role}")
    edit_window.destroy()

# Function to view users and roles
def view_users_and_roles():
    users_and_roles = tk.Toplevel(root)
    users_and_roles.title("Users and Roles")
    
    ttk.Label(users_and_roles, text="Current Users and Roles").pack(pady=10)
    
    tree = ttk.Treeview(users_and_roles, columns=("Username", "Role"), show='headings')
    tree.heading("Username", text="Username")
    tree.heading("Role", text="Role")
    
    for user in users_data:
        tree.insert("", tk.END, values=(user["username"], user["role"]))
    
    tree.pack(pady=10)

# Create the main application window
root = tk.Tk()
root.title("Login Page")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Create frames for each tab
login_frame = ttk.Frame(notebook, width=400, height=300)
register_frame = ttk.Frame(notebook, width=400, height=300)

login_frame.pack(fill='both', expand=True)
register_frame.pack(fill='both', expand=True)

# Add frames to notebook
notebook.add(login_frame, text='Login')
notebook.add(register_frame, text='Register')

# Login Tab
ttk.Label(login_frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
login_username_entry = ttk.Entry(login_frame)
login_username_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(login_frame, text="Password").grid(row=1, column=0, padx=10, pady=10)
login_password_entry = ttk.Entry(login_frame, show='*')
login_password_entry.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(login_frame, text="Role").grid(row=2, column=0, padx=10, pady=10)
login_role = ttk.Combobox(login_frame, values=["Admin", "User"])
login_role.grid(row=2, column=1, padx=10, pady=10)

login_button = ttk.Button(login_frame, text="Login", command=login)
login_button.grid(row=3, column=1, padx=10, pady=10)

# Register Tab
ttk.Label(register_frame, text="Username").grid(row=0, column=0, padx=10, pady=10)
register_username_entry = ttk.Entry(register_frame)
register_username_entry.grid(row=0, column=1, padx=10, pady=10)

ttk.Label(register_frame, text="Password").grid(row=1, column=0, padx=10, pady=10)
register_password_entry = ttk.Entry(register_frame, show='*')
register_password_entry.grid(row=1, column=1, padx=10, pady=10)

ttk.Label(register_frame, text="Confirm Password").grid(row=2, column=0, padx=10, pady=10)
register_confirm_password_entry = ttk.Entry(register_frame, show='*')
register_confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

ttk.Label(register_frame, text="Email").grid(row=3, column=0, padx=10, pady=10)
register_email_entry = ttk.Entry(register_frame)
register_email_entry.grid(row=3, column=1, padx=10, pady=10)

ttk.Label(register_frame, text="Phone Number").grid(row=4, column=0, padx=10, pady=10)
register_phone_entry = ttk.Entry(register_frame)

register_phone_entry.grid(row=4, column=1, padx=10, pady=10)

register_button = ttk.Button(register_frame, text="Register", command=register)
register_button.grid(row=5, column=1, padx=10, pady=10)

# Run the application
root.mainloop()