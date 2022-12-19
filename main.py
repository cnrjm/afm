import tkinter as tk
from tkinter import filedialog
import os
import shutil

# Create the main window
window = tk.Tk()
window.title("File Management System")

# Define the function for the browse button
def browse_files():
  file_path = filedialog.askopenfilename()
  if not file_path:
    tk.messagebox.showerror("Error", "Please select a file")
  else:
    file_type = os.path.splitext(file_path)[1]  # Extract the file extension
    file_ext.delete(0, tk.END)
    file_ext.insert(0, file_type)

def select_copy_folder():
    directory = filedialog.askdirectory()
    if not directory:
      # Display an error message if the user cancels the dialog
      tk.messagebox.showerror("Error", "Please select a folder")
    else:
      copy_folder_textbox.delete(0, tk.END)
      copy_folder_textbox.insert(0, directory)

def select_paste_folder():
    directory = filedialog.askdirectory()
    if not directory:
      # Display an error message if the user cancels the dialog
      tk.messagebox.showerror("Error", "Please select a folder")
    else:
      paste_folder_textbox.delete(0, tk.END)
      paste_folder_textbox.insert(0, directory)

def copy_files(src_dir, dst_dir, file_ext):
  for root, dirs, files in os.walk(src_dir):
    for file in files:
      if file.endswith(file_ext):
        shutil.copy(os.path.join(root, file), dst_dir)

def afm_button_clicked():
  src_dir = copy_folder_textbox.get()
  dst_dir = paste_folder_textbox.get()
  file_ext = os.path.splitext(src_dir)[1]
  copy_files(src_dir, dst_dir, file_ext)

# Create a textbox and a browse button
file_ext = tk.Entry(window)
file_ext_button = tk.Button(window, text="SELECT FILE TYPE TO COPY", command=browse_files)

copy_folder_textbox = tk.Entry(window)
copy_button = tk.Button(window, text="SELECT FOLDER TO COPY FROM", command=select_copy_folder)

paste_folder_textbox = tk.Entry(window)
paste_button = tk.Button(window, text="SELECT FOLDER TO COPY TO", command=select_paste_folder)

# Place the widgets in the window
file_ext_button.grid(row=0, column=0, sticky="NSEW", padx=50, pady=50)
file_ext.grid(row=0, column=1, sticky="NSEW", padx=50, pady=50)

copy_button.grid(row=1, column=0, sticky="NSEW", padx=50, pady=50)
copy_folder_textbox.grid(row=1, column=1, sticky="NSEW", padx=50, pady=50)

paste_button.grid(row=2, column=0, sticky="NSEW", padx=50, pady=50)
paste_folder_textbox.grid(row=2, column=1, sticky="NSEW", padx=50, pady=50)

afm_button = tk.Button(window, text="START", command=afm_button_clicked)
afm_button.grid(row=3, column=0, sticky="NSEW", padx=50, pady=50)


# Run the main loop
window.mainloop()
