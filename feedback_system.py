import tkinter as tk
from tkinter import ttk, messagebox

class FeedbackSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Feedback System - Pharmacy Inventory")
        self.root.geometry("600x400")

        tk.Label(self.root, text="Customer Feedback", font=("Arial", 18)).pack(pady=10)

        # Feedback Entry
        tk.Label(self.root, text="Enter your feedback:").pack()
        self.feedback_entry = tk.Text(self.root, height=4, width=50)
        self.feedback_entry.pack(pady=5)

        tk.Button(self.root, text="Submit Feedback", width=20, command=self.submit_feedback).pack(pady=5)
        tk.Button(self.root, text="Back", width=15, command=self.go_back).pack(pady=10)


        # Feedback List
        tk.Label(self.root, text="Previous Feedback").pack(pady=10)
        self.tree = ttk.Treeview(self.root, columns=("ID", "Feedback"), show="headings")
        self.tree.heading("ID", text="Feedback ID")
        self.tree.heading("Feedback", text="Feedback")
        self.tree.pack(pady=10)

        self.load_dummy_feedback()

    def load_dummy_feedback(self):
        # Dummy data (Replace with database logic)
        data = [(1, "Great service!"), (2, "Good quality medicines.")]
        for item in data:
            self.tree.insert("", "end", values=item)

    def submit_feedback(self):
        feedback_text = self.feedback_entry.get("1.0", "end").strip()
        if feedback_text:
            new_id = len(self.tree.get_children()) + 1  # Generate ID
            self.tree.insert("", "end", values=(new_id, feedback_text))
            messagebox.showinfo("Success", "Feedback submitted successfully!")
        else:
            messagebox.showerror("Error", "Feedback cannot be empty!")

    def go_back(self):
        self.root.destroy()
        import subprocess
        subprocess.run(["python", "customer_dashboard.py"])

if __name__ == "__main__":
    root = tk.Tk()
    app = FeedbackSystem(root)
    root.mainloop()
