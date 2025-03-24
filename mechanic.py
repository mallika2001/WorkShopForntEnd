import tkinter as tk

class MechanicDashboard:
    def __init__(self, parent):
        self.parent = parent

        tk.Label(parent, text="Mechanic Dashboard", font=("Arial", 16)).pack(pady=10)

        tk.Button(parent, text="View Assigned Jobs", command=self.view_jobs).pack(fill=tk.X, pady=5)

    def view_jobs(self):
        print("Viewing assigned jobs")
