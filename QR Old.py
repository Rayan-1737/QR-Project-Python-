from tkinter import *
import qrcode
from PIL import Image, ImageTk
import time
from tkinter import messagebox
import os

# Create the main application window
root = Tk()
root.title("QR Code Generator")
root.geometry("600x700")  # Adjusted for extra features
root.config(bg="#F5F5F5")
root.resizable(False, False)

# Ensure the 'Qrcode' directory exists
os.makedirs("Qrcode", exist_ok=True)

# Function to generate QR Code and display it
def generate() -> None:
    """Generate a QR code from the given text/link and show it in the window."""
    name = title.get().strip()
    text = entry.get().strip()

    if not name or not text:
        messagebox.showwarning("Input Error", "Both Title and Text/Link fields must be filled!")
        return

    try:
        # Show a small delay for effect
        button.config(state=DISABLED, bg="white", fg="black")
        progress_label.config(text="Generating QR Code...")
        root.update_idletasks()
        time.sleep(1)  # Simulate processing time

        # Generate QR Code
        qr = qrcode.make(text)
        qr_image = qr.resize((250, 250))  # Adjusted QR Code size (250x250)

        # Display QR Code
        qr_image = ImageTk.PhotoImage(qr_image)
        qr_label.config(image=qr_image)
        qr_label.image = qr_image  # Keep reference to prevent garbage collection

        progress_label.config(text="QR Code Generated Successfully!")
        button.config(state=NORMAL, bg="white", fg="black")  # Reset button state
    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR Code: {str(e)}")

# Add title text with larger font
Label(
    root,
    text="QR Generator",  # Simplified title
    font=("Arial", 30, "bold"),  # Larger font for impact
    fg="#0078D4",  # Blue color for vibrancy
    bg="#F5F5F5",  # Light background
    pady=20  # Padding at the top for spacing
).place(x=200, y=30)  # Positioned near the top of the window

# Title entry
Label(root, text="Enter Title", fg="black", bg="#F5F5F5", font=("Arial", 14, "bold")).place(x=150, y=150)
title = Entry(root, width=35, font=("Arial", 15), bg="#E0E0E0", fg="black", insertbackground="black")  # Black cursor
title.place(x=150, y=180)

# Text/Link entry
Label(root, text="Enter Text or Link", fg="black", bg="#F5F5F5", font=("Arial", 14, "bold")).place(x=150, y=220)
entry = Entry(root, width=35, font=("Arial", 15), bg="#E0E0E0", fg="black", insertbackground="black")  # Black cursor
entry.place(x=150, y=250)

# QR Code display area
qr_label = Label(root, bg="#F5F5F5")
qr_label.place(x=175, y=400)

# Generate button with hover effect
def on_enter(e):
    button.config(bg="#00BFFF", fg="black")

def on_leave(e):
    button.config(bg="white", fg="black")

# Move the button further to the right
button = Button(
    root,
    text="Generate QR Code",
    width=20,
    height=2,
    bg="white",
    fg="black",
    font=("Arial", 15, "bold"),
    command=generate
)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.place(x=210, y=300)  # Positioned further right below the "Enter Text or Link" box

# Progress label for feedback
progress_label = Label(root, text="", fg="black", bg="#F5F5F5", font=("Arial", 12))
progress_label.place(x=150, y=360)

# Footer text for "Scan with confidence"
Label(
    root,
    text="Scan with confidence! Built by 'Rayan' 🛠️",
    fg="black",
    bg="#F5F5F5",
    font=("Arial", 10, "italic")
).place(x=590, y=670, anchor="se")  # Positioned in the bottom-right corner

# Footer text for "Made by Rayan. All rights reserved © 2025"
Label(
    root,
    text="Made by Rayan. All rights reserved © 2025",
    fg="black",
    bg="#F5F5F5",
    font=("Arial", 12, "italic")
).place(x=590, y=690, anchor="se")  # Positioned below the previous footer

root.mainloop()
