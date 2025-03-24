import tkinter as tk
from tkinter import ttk, messagebox

class FeedbackPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")

        self.feedback_list = [
            {"ID": 1, "Customer": "John Doe", "Order ID": 101, "Rating": 5, "Comments": "Excellent service!", "Date": "2025-03-22"},
            {"ID": 2, "Customer": "Jane Smith", "Order ID": 102, "Rating": 4, "Comments": "Very good, but slight delay.", "Date": "2025-03-23"},
        ]

        tk.Label(self, text="Customer Feedback & Reviews", font=("Arial", 16, "bold"), bg="#ECF0F1").pack(pady=10)

        # Table
        self.tree = ttk.Treeview(self, columns=("ID", "Customer", "Order ID", "Rating", "Comments", "Date"), show="headings")
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

        tk.Label(form_frame, text="Order ID:").grid(row=0, column=2)
        self.order_id_entry = tk.Entry(form_frame)
        self.order_id_entry.grid(row=0, column=3, padx=10)

        tk.Label(form_frame, text="Rating (1-5):").grid(row=1, column=0)
        self.rating_entry = tk.Entry(form_frame)
        self.rating_entry.grid(row=1, column=1, padx=10)

        tk.Label(form_frame, text="Comments:").grid(row=1, column=2)
        self.comments_entry = tk.Entry(form_frame)
        self.comments_entry.grid(row=1, column=3, padx=10)

        tk.Label(form_frame, text="Date:").grid(row=2, column=0)
        self.date_entry = tk.Entry(form_frame)
        self.date_entry.grid(row=2, column=1, padx=10)

        # Buttons
        button_frame = tk.Frame(self, bg="#ECF0F1")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Feedback", bg="#27AE60", fg="white", command=self.add_feedback).pack(side="left", padx=10)
        tk.Button(button_frame, text="Update Feedback", bg="#F39C12", fg="white", command=self.update_feedback).pack(side="left", padx=10)
        tk.Button(button_frame, text="Delete Feedback", bg="#E74C3C", fg="white", command=self.delete_feedback).pack(side="left", padx=10)

    def load_data(self):
        for fb in self.feedback_list:
            self.tree.insert("", "end", values=(fb["ID"], fb["Customer"], fb["Order ID"], fb["Rating"], fb["Comments"], fb["Date"]))

    def add_feedback(self):
        new_id = len(self.feedback_list) + 1
        new_fb = {
            "ID": new_id,
            "Customer": self.customer_entry.get(),
            "Order ID": self.order_id_entry.get(),
            "Rating": int(self.rating_entry.get()),
            "Comments": self.comments_entry.get(),
            "Date": self.date_entry.get()
        }
        self.feedback_list.append(new_fb)
        self.tree.insert("", "end", values=(new_id, new_fb["Customer"], new_fb["Order ID"], new_fb["Rating"], new_fb["Comments"], new_fb["Date"]))
        messagebox.showinfo("Success", "Feedback added successfully!")
        self.clear_fields()

    def update_feedback(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a feedback to update.")
            return

        idx = self.tree.index(selected)
        updated = {
            "ID": self.feedback_list[idx]["ID"],
            "Customer": self.customer_entry.get(),
            "Order ID": self.order_id_entry.get(),
            "Rating": int(self.rating_entry.get()),
            "Comments": self.comments_entry.get(),
            "Date": self.date_entry.get()
        }

        self.feedback_list[idx] = updated
        self.tree.item(selected, values=(updated["ID"], updated["Customer"], updated["Order ID"], updated["Rating"], updated["Comments"], updated["Date"]))
        messagebox.showinfo("Success", "Feedback updated successfully!")
        self.clear_fields()

    def delete_feedback(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a feedback to delete.")
            return

        idx = self.tree.index(selected)
        del self.feedback_list[idx]
        self.tree.delete(selected)
        messagebox.showinfo("Success", "Feedback deleted successfully!")

    def clear_fields(self):
        self.customer_entry.delete(0, tk.END)
        self.order_id_entry.delete(0, tk.END)
        self.rating_entry.delete(0, tk.END)
        self.comments_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
