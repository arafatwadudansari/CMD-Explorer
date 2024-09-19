import tkinter as tk
from tkinter import messagebox
import subprocess

# Run a command in a new CMD window
def run_command(command):
    subprocess.run('start cmd /k ' + '"' + command + '"', shell=True)

# Execute the selected command
def execute_command():
    cmd = command_var.get()  # Get the selected command
    if cmd == 'ping':
        command = 'ping ' + ping_entry.get()  # Target for ping
    elif cmd == 'tracert':
        command = 'tracert ' + tracert_entry.get()  # Target for tracert
    elif cmd == 'nslookup':
        command = 'nslookup ' + nslookup_entry.get()  # Target for nslookup
    elif cmd == 'pathping':
        command = 'pathping ' + pathping_entry.get()  # Target for pathping
    elif cmd == 'ipconfig':
        command = 'ipconfig'  # No extra input needed
    elif cmd == 'netstat':
        command = 'netstat'  # No extra input needed
    else:
        messagebox.showwarning("Warning", "Please select a command.")
        return
    run_command(command)

# Set up the main window
root = tk.Tk()
root.title("CMD Explorer")

# Variable for command selection
command_var = tk.StringVar()

# Instructions label
tk.Label(root, text="Select a command to execute:").grid(row=0, column=0, columnspan=2, pady=10)

# Entry fields for commands needing extra details
ping_entry = tk.Entry(root, width=20)
tracert_entry = tk.Entry(root, width=20)
nslookup_entry = tk.Entry(root, width=20)
pathping_entry = tk.Entry(root, width=20)

# Radio buttons for command options
tk.Radiobutton(root, text="Ping", variable=command_var, value="ping").grid(row=1, column=0, sticky="w")
ping_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

tk.Radiobutton(root, text="Tracert", variable=command_var, value="tracert").grid(row=2, column=0, sticky="w")
tracert_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Radiobutton(root, text="Ipconfig", variable=command_var, value="ipconfig").grid(row=3, column=0, sticky="w")

tk.Radiobutton(root, text="Nslookup", variable=command_var, value="nslookup").grid(row=4, column=0, sticky="w")
nslookup_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

tk.Radiobutton(root, text="Netstat", variable=command_var, value="netstat").grid(row=5, column=0, sticky="w")

tk.Radiobutton(root, text="Pathping", variable=command_var, value="pathping").grid(row=6, column=0, sticky="w")
pathping_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# Button to execute the command
tk.Button(root, text="Execute", command=execute_command).grid(row=7, column=0, columnspan=2, pady=20)

# Start the GUI
root.mainloop()
