import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def convert_jpeg_to_png(input_path, output_path):
    try:
        # Open the JPEG image
        with Image.open(input_path) as img:
            # Save as PNG
            img.save(output_path, 'PNG')
        return True
    except Exception as e:
        print(f"Error converting image: {e}")
        return False

def select_jpeg_file():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg *.jpeg")])
    return file_path

def select_output_directory():
    dir_path = filedialog.askdirectory()
    return dir_path

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Select input JPEG file
    input_path = select_jpeg_file()
    if not input_path:
        messagebox.showerror("Error", "No input file selected.")
        return

    # Select output directory
    output_dir = select_output_directory()
    if not output_dir:
        messagebox.showerror("Error", "No output directory selected.")
        return

    # Generate output file path
    input_filename = os.path.basename(input_path)
    output_filename = os.path.splitext(input_filename)[0] + ".png"
    output_path = os.path.join(output_dir, output_filename)

    # Convert JPEG to PNG
    success = convert_jpeg_to_png(input_path, output_path)

    if success:
        messagebox.showinfo("Success", f"Image converted successfully!\nSaved as: {output_path}")
    else:
        messagebox.showerror("Error", "Failed to convert image. Check console for details.")

if __name__ == "__main__":
    main()
