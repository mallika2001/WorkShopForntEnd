import tkinter as tk
from tkinter import ttk
 
def submit_review():
    customer_id = customer_id_entry.get()
    order_id = order_id_entry.get()
    rating = rating_entry.get()
    comments = comments_entry.get()
    review_date = review_date_entry.get()
    
    print(f"Review Submitted: {customer_id}, {order_id}, {rating}, {comments}, {review_date}")
 
root = tk.Tk()
root.title("Customer Feedback & Reviews")
root.geometry("400x300")
 
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky="nsew")
 
ttk.Label(frame, text="Customer ID:").grid(row=0, column=0, sticky="w", pady=5)
customer_id_entry = ttk.Entry(frame, width=40)
customer_id_entry.grid(row=0, column=1, pady=5)
 
ttk.Label(frame, text="Order ID:").grid(row=1, column=0, sticky="w", pady=5)
order_id_entry = ttk.Entry(frame, width=40)
order_id_entry.grid(row=1, column=1, pady=5)
 
ttk.Label(frame, text="Rating (1-5 Stars):").grid(row=2, column=0, sticky="w", pady=5)
rating_entry = ttk.Entry(frame, width=40)
rating_entry.grid(row=2, column=1, pady=5)
 
ttk.Label(frame, text="Comments:").grid(row=3, column=0, sticky="w", pady=5)
comments_entry = ttk.Entry(frame, width=40)
comments_entry.grid(row=3, column=1, pady=5)
 
ttk.Label(frame, text="Review Date:").grid(row=4, column=0, sticky="w", pady=5)
review_date_entry = ttk.Entry(frame, width=40)
review_date_entry.grid(row=4, column=1, pady=5)
 
submit_button = ttk.Button(frame, text="Submit", command=submit_review)
submit_button.grid(row=5, column=0, columnspan=2, pady=20)
 
root.mainloop()