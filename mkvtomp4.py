import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import ffmpeg
import os
from threading import Thread

# Function to convert MKV to MP4
def convert_mkv_to_mp4(input_file, output_file, progress_label):
    try:
        # Starting FFmpeg conversion
        progress_label.config(text="Converting...")
        ffmpeg.input(input_file).output(output_file).run(overwrite_output=True)
        progress_label.config(text="Conversion complete!")
        messagebox.showinfo("Success", "File converted successfully!")
    except Exception as e:
        progress_label.config(text="Conversion failed!")
        messagebox.showerror("Error", f"Conversion failed: {e}")

# Function to browse for MKV file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MKV files", "*.mkv")])
    if file_path:
        input_path_var.set(file_path)
        output_path_var.set(file_path.replace(".mkv", ".mp4"))

# Function to start conversion in a separate thread
def start_conversion():
    input_file = input_path_var.get()
    output_file = output_path_var.get()
    if not input_file or not output_file:
        messagebox.showwarning("Warning", "Please select a valid MKV file and specify an output file!")
        return

    # Starting conversion thread
    Thread(target=convert_mkv_to_mp4, args=(input_file, output_file, progress_label)).start()

# Creating the main application window
root = tk.Tk()
root.title("MKV to MP4 Converter")
root.geometry("400x250")
root.configure(bg="#333333")  # Dark background

# Adding title label
title_label = tk.Label(root, text="MKV to MP4 Converter", font=("Helvetica", 18, "bold"), fg="white", bg="#333333")
title_label.pack(pady=10)

# Input file selection
input_frame = tk.Frame(root, bg="#333333")
input_frame.pack(pady=5)
input_label = tk.Label(input_frame, text="Select MKV File:", font=("Helvetica", 12), fg="white", bg="#333333")
input_label.pack(side=tk.LEFT, padx=5)
input_path_var = tk.StringVar()
input_entry = tk.Entry(input_frame, textvariable=input_path_var, width=25, font=("Helvetica", 10))
input_entry.pack(side=tk.LEFT, padx=5)
browse_button = tk.Button(input_frame, text="Browse", command=browse_file, bg="#4CAF50", fg="white")
browse_button.pack(side=tk.LEFT, padx=5)

# Output file path entry
output_frame = tk.Frame(root, bg="#333333")
output_frame.pack(pady=5)
output_label = tk.Label(output_frame, text="Save as MP4:", font=("Helvetica", 12), fg="white", bg="#333333")
output_label.pack(side=tk.LEFT, padx=5)
output_path_var = tk.StringVar()
output_entry = tk.Entry(output_frame, textvariable=output_path_var, width=25, font=("Helvetica", 10))
output_entry.pack(side=tk.LEFT, padx=5)

# Conversion progress label
progress_label = tk.Label(root, text="", font=("Helvetica", 10), fg="white", bg="#333333")
progress_label.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=start_conversion, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", width=10)
convert_button.pack(pady=10)

# Running the main GUI loop
root.mainloop()
