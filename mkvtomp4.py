import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk  # Modern UI
import ffmpeg
import os
from threading import Thread

# 🔹 Set the full path to ffmpeg.exe (Change this to your actual path)
FFMPEG_PATH = r"C:\\ffmpeg\\bin\\ffmpeg.exe"  # Example path - Update this!

# Function to convert MKV to MP4
def convert_mkv_to_mp4(input_file, output_file):
    try:
        root.after(0, lambda: status_label.config(text="Converting...", bootstyle="info"))
        root.after(0, lambda: progress_bar.start())

        # Run FFmpeg conversion using the full path
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec="copy", acodec="aac")
            .run(cmd=FFMPEG_PATH, overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )

        # Update UI on success
        root.after(0, lambda: status_label.config(text="✅ Conversion complete!", bootstyle="success"))
        root.after(0, lambda: progress_bar.stop())
        root.after(0, lambda: messagebox.showinfo("Success", "File converted successfully!"))

    except ffmpeg.Error as e:
        error_msg = e.stderr.decode() if e.stderr else str(e)
        root.after(0, lambda: handle_error(error_msg))  

    except Exception as e:
        error_msg = str(e)  
        root.after(0, lambda: handle_error(error_msg))  

# Function to handle errors
def handle_error(error_msg):
    status_label.config(text="❌ Conversion failed!", bootstyle="danger")
    progress_bar.stop()
    messagebox.showerror("Error", f"Error: {error_msg}")

# Function to browse for MKV file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MKV files", "*.mkv")])
    if file_path:
        input_path_var.set(file_path)
        output_path_var.set(file_path.rsplit(".", 1)[0] + ".mp4")

# Function to start conversion in a separate thread
def start_conversion():
    input_file = input_path_var.get()
    output_file = output_path_var.get()

    if not input_file or not output_file:
        messagebox.showwarning("Warning", "Please select a valid MKV file and specify an output file!")
        return

    convert_button.config(state=tk.DISABLED)
    status_label.config(text="🔄 Starting conversion...", bootstyle="warning")

    # Start conversion in a new thread
    thread = Thread(target=lambda: (
        convert_mkv_to_mp4(input_file, output_file),
        root.after(0, lambda: convert_button.config(state=tk.NORMAL))
    ))
    thread.start()

# Create the main application window
root = ttk.Window(themename="darkly")  # Dark modern theme
root.title("MKV to MP4 Converter")
root.geometry("450x300")
root.resizable(False, False)

# Title label
title_label = ttk.Label(root, text="🎬 MKV to MP4 Converter", font=("Helvetica", 18, "bold"), bootstyle="primary")
title_label.pack(pady=10)

# Input file selection
input_frame = ttk.Frame(root)
input_frame.pack(pady=5)

input_label = ttk.Label(input_frame, text="Select MKV File:", font=("Helvetica", 12))
input_label.pack(side=tk.LEFT, padx=5)

input_path_var = tk.StringVar()
input_entry = ttk.Entry(input_frame, textvariable=input_path_var, width=30)
input_entry.pack(side=tk.LEFT, padx=5)

browse_button = ttk.Button(input_frame, text="Browse", command=browse_file, bootstyle="success")
browse_button.pack(side=tk.LEFT, padx=5)

# Output file path
output_frame = ttk.Frame(root)
output_frame.pack(pady=5)

output_label = ttk.Label(output_frame, text="Save as MP4:", font=("Helvetica", 12))
output_label.pack(side=tk.LEFT, padx=5)

output_path_var = tk.StringVar()
output_entry = ttk.Entry(output_frame, textvariable=output_path_var, width=30)
output_entry.pack(side=tk.LEFT, padx=5)

# Status Label
status_label = ttk.Label(root, text="Ready to convert", font=("Helvetica", 10), bootstyle="info")
status_label.pack(pady=5)

# Progress Bar
progress_bar = ttk.Progressbar(root, mode="indeterminate", bootstyle="success")
progress_bar.pack(fill=tk.X, padx=20, pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=start_conversion, bootstyle="primary", width=15)
convert_button.pack(pady=10)

# Run the main GUI loop
root.mainloop()
import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk  # Modern UI
import ffmpeg
import os
from threading import Thread

# 🔹 Set the full path to ffmpeg.exe (Change this to your actual path)
FFMPEG_PATH = r"C:\\ffmpeg\\bin\\ffmpeg.exe"  # Example path - Update this!

# Function to convert MKV to MP4
def convert_mkv_to_mp4(input_file, output_file):
    try:
        root.after(0, lambda: status_label.config(text="Converting...", bootstyle="info"))
        root.after(0, lambda: progress_bar.start())

        # Run FFmpeg conversion using the full path
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec="copy", acodec="aac")
            .run(cmd=FFMPEG_PATH, overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )

        # Update UI on success
        root.after(0, lambda: status_label.config(text="✅ Conversion complete!", bootstyle="success"))
        root.after(0, lambda: progress_bar.stop())
        root.after(0, lambda: messagebox.showinfo("Success", "File converted successfully!"))

    except ffmpeg.Error as e:
        error_msg = e.stderr.decode() if e.stderr else str(e)
        root.after(0, lambda: handle_error(error_msg))  

    except Exception as e:
        error_msg = str(e)  
        root.after(0, lambda: handle_error(error_msg))  

# Function to handle errors
def handle_error(error_msg):
    status_label.config(text="❌ Conversion failed!", bootstyle="danger")
    progress_bar.stop()
    messagebox.showerror("Error", f"Error: {error_msg}")

# Function to browse for MKV file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MKV files", "*.mkv")])
    if file_path:
        input_path_var.set(file_path)
        output_path_var.set(file_path.rsplit(".", 1)[0] + ".mp4")

# Function to start conversion in a separate thread
def start_conversion():
    input_file = input_path_var.get()
    output_file = output_path_var.get()

    if not input_file or not output_file:
        messagebox.showwarning("Warning", "Please select a valid MKV file and specify an output file!")
        return

    convert_button.config(state=tk.DISABLED)
    status_label.config(text="🔄 Starting conversion...", bootstyle="warning")

    # Start conversion in a new thread
    thread = Thread(target=lambda: (
        convert_mkv_to_mp4(input_file, output_file),
        root.after(0, lambda: convert_button.config(state=tk.NORMAL))
    ))
    thread.start()

# Create the main application window
root = ttk.Window(themename="darkly")  # Dark modern theme
root.title("MKV to MP4 Converter")
root.geometry("450x300")
root.resizable(False, False)

# Title label
title_label = ttk.Label(root, text="🎬 MKV to MP4 Converter", font=("Helvetica", 18, "bold"), bootstyle="primary")
title_label.pack(pady=10)

# Input file selection
input_frame = ttk.Frame(root)
input_frame.pack(pady=5)

input_label = ttk.Label(input_frame, text="Select MKV File:", font=("Helvetica", 12))
input_label.pack(side=tk.LEFT, padx=5)

input_path_var = tk.StringVar()
input_entry = ttk.Entry(input_frame, textvariable=input_path_var, width=30)
input_entry.pack(side=tk.LEFT, padx=5)

browse_button = ttk.Button(input_frame, text="Browse", command=browse_file, bootstyle="success")
browse_button.pack(side=tk.LEFT, padx=5)

# Output file path
output_frame = ttk.Frame(root)
output_frame.pack(pady=5)

output_label = ttk.Label(output_frame, text="Save as MP4:", font=("Helvetica", 12))
output_label.pack(side=tk.LEFT, padx=5)

output_path_var = tk.StringVar()
output_entry = ttk.Entry(output_frame, textvariable=output_path_var, width=30)
output_entry.pack(side=tk.LEFT, padx=5)

# Status Label
status_label = ttk.Label(root, text="Ready to convert", font=("Helvetica", 10), bootstyle="info")
status_label.pack(pady=5)

# Progress Bar
progress_bar = ttk.Progressbar(root, mode="indeterminate", bootstyle="success")
progress_bar.pack(fill=tk.X, padx=20, pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=start_conversion, bootstyle="primary", width=15)
convert_button.pack(pady=10)

# Run the main GUI loop
root.mainloop()
