import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    # Simple validation
    if not username or not password or not email:
        messagebox.showwarning("Warning", "Please fill all fields!")
        return

    # Save data to a file (for demonstration purposes)
    with open("registration_data.txt", "a") as f:
        f.write(f"Username: {username}, Password: {password}, Email: {email}\n")

    messagebox.showinfo("Success", "Registration Successful!")

    # Clear the fields
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Registration Page")
root.geometry("300x250")  # Set a fixed size for the window

# Create and place labels and entries for username, password, and email
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, show='*')
entry_password.pack(pady=5)

label_email = tk.Label(root, text="Email:")
label_email.pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack(pady=5)

# Create and place the Register button
register_button = tk.Button(root, text="Register", command=register)
register_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
