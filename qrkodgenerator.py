import tkinter as tk
import segno
from tkinter import filedialog
from PIL import Image, ImageTk

def generate_qr_code():
    url = url_entry.get()
    qr = segno.make(url)
    qr_image = qr.save_as_png(scale=5)
    qr_image = Image.open(qr_image)
    qr_image = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image)
    qr_label.image = qr_image

def save_qr_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        qr.save(file_path)

root = tk.Tk()
root.geometry("600x400")

url_frame = tk.Frame(root)
url_frame.pack(pady=20)

url_label = tk.Label(url_frame, text="Enter URL:")
url_label.pack(side="left")

url_entry = tk.Entry(url_frame, width=50)
url_entry.pack(side="left")

generate_button = tk.Button(url_frame, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(side="left")

qr_frame = tk.Frame(root)
qr_frame.pack()

qr_label = tk.Label(qr_frame)
qr_label.pack()

save_button = tk.Button(qr_frame, text="Save QR Code", command=save_qr_code)
save_button.pack()

root.mainloop()
