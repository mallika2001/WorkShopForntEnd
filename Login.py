import tkinter as tk
from tkinter import messagebox
from main import MainApp  # Make sure main.py has MainApp class

# Sample user database
USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "mechanic": {"password": "mech123", "role": "Mechanic"},
    "customer": {"password": "cust123", "role": "Customer"}
}

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Workshop Login")
        self.geometry("350x250")
        self.configure(bg="#ECF0F1")

        tk.Label(self, text="Login", font=("Arial", 18, "bold"), bg="#ECF0F1").pack(pady=20)

        tk.Label(self, text="Username:", bg="#ECF0F1").pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        tk.Label(self, text="Password:", bg="#ECF0F1").pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        tk.Button(self, text="Login", bg="#3498DB", fg="white", command=self.login).pack(pady=15)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = USERS.get(username)
        if user and user["password"] == password:
            messagebox.showinfo("Login Successful", f"Welcome, {username} ({user['role']})")
            self.destroy()
            MainApp(user["role"]).mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

if __name__ == "__main__":
    LoginPage().mainloop()
