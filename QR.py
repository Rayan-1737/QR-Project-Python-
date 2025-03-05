import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox, filedialog

# Color schemes for themes
themes = {
    "Cyber Theme": {"fill_color": "#00CED1", "back_color": "#000000"},  # Neon blue on black
    "Minimal White": {"fill_color": "#FFB6C1", "back_color": "#FFFFFF"},  # Pastel pink on white
}

# Set up the main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x600")  # Adjusted window size

# Function to load text from a file
def load_text_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, file.read())

# Text input area
text_input = tk.Text(root, height=5, width=50)
text_input.pack(pady=10)

# Drop File Button
drop_file_button = tk.Button(root, text="Drop File", command=load_text_file)
drop_file_button.pack(pady=5)

# Theme selection
theme_frame = tk.Frame(root)
theme_frame.pack(pady=5)
theme_var = tk.StringVar(value="Cyber Theme")
tk.Radiobutton(theme_frame, text="Cyber Theme", variable=theme_var, value="Cyber Theme").pack(side=tk.LEFT)
tk.Radiobutton(theme_frame, text="Minimal White", variable=theme_var, value="Minimal White").pack(side=tk.LEFT)

# Buttons
generate_button = tk.Button(root, text="Generate QR Code", command=lambda: generate_qr())
generate_button.pack(pady=5)
preview_button = tk.Button(root, text="Scan Preview", command=lambda: preview_qr())
preview_button.pack(pady=5)
save_button = tk.Button(root, text="Save QR Code", command=lambda: save_qr(), state=tk.DISABLED)
save_button.pack(pady=5)

# QR code display area
display_frame = tk.Frame(root)
display_frame.pack(pady=10)
qr_label = tk.Label(display_frame)
qr_label.pack()

# Global variable for the current QR code image
current_img = None

# Function to create a QR code image
def create_qr_image(text, fill_color, back_color):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    return qr.make_image(fill_color=fill_color, back_color=back_color)

# Generate QR code
def generate_qr():
    global current_img
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter some text or URL.")
        return
    theme = theme_var.get()
    fill_color = themes[theme]["fill_color"]
    back_color = themes[theme]["back_color"]
    img = create_qr_image(text, fill_color, back_color)
    display_qr(img)
    save_button.config(state=tk.NORMAL)
    current_img = img

# Preview QR code in a new window
def preview_qr():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter some text or URL.")
        return
    theme = theme_var.get()
    fill_color = themes[theme]["fill_color"]
    back_color = themes[theme]["back_color"]
    img = create_qr_image(text, fill_color, back_color)
    preview_window = tk.Toplevel(root)
    preview_window.title("Scan Preview")
    photo = ImageTk.PhotoImage(img)
    img_label = tk.Label(preview_window, image=photo)
    img_label.image = photo  # Keep reference to avoid garbage collection
    img_label.pack(pady=10)
    text_label = tk.Label(preview_window, text=f"Encoded text: {text}")
    text_label.pack(pady=5)
    tk.Button(preview_window, text="Close", command=preview_window.destroy).pack(pady=5)

# Save the QR code image
def save_qr():
    global current_img
    if not current_img:
        messagebox.showerror("Error", "No QR code to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        current_img.save(file_path)
        messagebox.showinfo("Success", "QR code saved successfully.")

# Display QR Code
def display_qr(img):
    photo = ImageTk.PhotoImage(img)
    qr_label.config(image=photo)
    qr_label.image = photo  # Keep reference to avoid garbage collection

# Start the application
root.mainloop()
