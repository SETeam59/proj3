import tkinter as tk
from tkinter import ttk, simpledialog
from PIL import Image, ImageTk, ImageFilter
import subprocess
import re

# List of predefined GITS commands for auto-complete
GITS_COMMANDS = [
    "hello_world", "cmd_history", "set", "add", "commit", "create", "upstream", "profile", "sync",
    "super-reset", "rebase", "reset", "push", "checkout", "unstage", "status", "diff",
    "init", "all-branch", "remote-branch", "commit_with_test", "stats", "commit_tree",
    "tag", "describe"
]


# Function to add a command to the command history file
def add_to_command_history(command):
    history_file_path = 'command_history.txt'
    history = get_command_history()
    history.append(command)
    write_command_history(history, history_file_path)
    refresh_command_history_menu()

# Add this function to refresh the command history menu
def refresh_command_history_menu():
    history = get_command_history()

    # Destroy previous command history menu
    if hasattr(window, "command_history_menu"):
        window.command_history_menu.destroy()

    # Create a new command history menu
    command_history_menu = tk.Menu(command_history_button, tearoff=0)
    for item in history:
        command_history_menu.add_command(label=item, command=lambda value=item: command_entry_var.set(value))
    command_history_button['menu'] = command_history_menu

    # Save the reference to the command history menu
    window.command_history_menu = command_history_menu

# Function to get the command history
def get_command_history():
    try:
        with open('command_history.txt', 'r') as file:
            history = [line.strip() for line in file.readlines()]
        return history
    except FileNotFoundError:
        return []
    
# Function to write the command history to a file
def write_command_history(history, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write('\n'.join(history))
    except Exception as e:
        print(f"Error writing command history to file: {str(e)}")

# Function to filter auto-complete options based on user input
def autocomplete_filter(user_input):
    return [command for command in GITS_COMMANDS if command.startswith(user_input)]

# Function to handle auto-complete when a key is pressed
def handle_autocomplete(event):
    global command_entry
    current_text = command_entry_var.get()

    # Remove the placeholder text when the user starts typing
    if current_text == command_entry_placeholder:
        command_entry_var.set("")
        return

    current_cursor_position = command_entry.index(tk.INSERT)

    # Get the word to be completed
    word_to_complete = re.search(r'\S*$', current_text[:current_cursor_position]).group(0)

    # Get the options to display in auto-complete
    options = autocomplete_filter(word_to_complete)

    # If the suggestion window is open, handle the Tab and Enter keys
    if hasattr(window, "suggestion_window") and window.suggestion_window.winfo_exists():
        if event.keysym == "Tab" or event.keysym == "Return":
            selected_option = window.suggestion_window.suggestion_listbox.get(tk.ACTIVE)
            if selected_option:
                command_entry_var.set(selected_option)
                window.suggestion_window.destroy()
            return

    # Show auto-complete suggestions
    show_autocomplete_suggestions(options)


# Function to show auto-complete suggestions in a lighter-shaded window
def show_autocomplete_suggestions(options):
    # Destroy the previous suggestion window
    if hasattr(window, "suggestion_window") and window.suggestion_window.winfo_exists():
        window.suggestion_window.destroy()

    # Create a new suggestion window
    suggestion_window = tk.Toplevel(window)
    suggestion_window.wm_overrideredirect(True)  # Remove window border
    suggestion_window.wm_geometry("+%d+%d" % (window.winfo_rootx() + command_entry.winfo_x(),
                                              window.winfo_rooty() + command_entry.winfo_y() +
                                              command_entry.winfo_height()))

    # Create a listbox for auto-complete options
    suggestion_listbox = tk.Listbox(suggestion_window, font=("Arial", 12), relief="solid", borderwidth=2,
                                    bg="#F0F0F0")  # Lighter shade background
    suggestion_listbox.pack()

    # Show auto-complete suggestions
    for option in options:
        suggestion_listbox.insert(tk.END, option)

    # Bind events for navigation and completion
    suggestion_listbox.bind("<ButtonRelease-1>", lambda event: insert_autocomplete(event, suggestion_window))
    suggestion_listbox.bind("<Return>", lambda event: insert_autocomplete(event, suggestion_window))
    suggestion_listbox.bind("<Tab>", lambda event: insert_autocomplete(event, suggestion_window))
    suggestion_listbox.bind("<Up>", lambda event: move_up(event, suggestion_listbox))
    suggestion_listbox.bind("<Down>", lambda event: move_down(event, suggestion_listbox))

    # Save the reference to the suggestion window and listbox
    window.suggestion_window = suggestion_window
    window.suggestion_listbox = suggestion_listbox

# Function to insert selected auto-complete option into the entry
def insert_autocomplete(event, suggestion_window):
    selected_option = event.widget.get(event.widget.curselection())
    command_entry_var.set(selected_option)

    # Destroy the suggestion window
    suggestion_window.destroy()

# Function to move selection up in auto-complete suggestions
def move_up(event, suggestion_listbox):
    current_index = suggestion_listbox.curselection()
    if current_index and current_index[0] > 0:
        suggestion_listbox.selection_clear(current_index)
        suggestion_listbox.selection_set(current_index[0] - 1)

# Function to move selection down in auto-complete suggestions
def move_down(event, suggestion_listbox):
    current_index = suggestion_listbox.curselection()
    if current_index and current_index[0] < len(suggestion_listbox.get(0, tk.END)) - 1:
        suggestion_listbox.selection_clear(current_index)
        suggestion_listbox.selection_set(current_index[0] + 1)

# Function to execute GITS command
def execute_gits_command():
    command = command_entry_var.get().strip()

    if not command:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Empty command. Please enter a valid GITS command.")
        return

    if command not in GITS_COMMANDS:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: Unknown command '{command}'. Please enter a valid GITS command.")
        return

    command = re.findall(r'[^"\s]+|"[^"]*"', command)

    command_list = ['python3', 'code/gits.py']
    for sub_c in command:
        command_list.append(sub_c)

    try:
        # Execute the GITS command and capture the output
        result = subprocess.check_output(command_list, stderr=subprocess.STDOUT, text=True)
        result_text.delete(1.0, tk.END)  # Clear previous output
        result_text.insert(tk.END, result)

        # Add the executed command to the history
        add_to_command_history(command_entry_var.get().strip())

    except subprocess.CalledProcessError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: " + e.output)
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "An error occurred: " + str(e))

def show_command_history():
    # Unbind KeyRelease event temporarily
    command_entry.unbind("<KeyRelease>")
    
    # Get the latest command history
    history = get_command_history()

    # Destroy previous command history menu
    if hasattr(window, "command_history_menu"):
        window.command_history_menu.destroy()

    # Create a new command history menu
    command_history_menu = tk.Menu(command_history_button, tearoff=0)
    for item in history:
        command_history_menu.add_command(label=item, command=lambda value=item: command_entry_var.set(value))
    command_history_button['menu'] = command_history_menu

    if history:
        selected_item = simpledialog.askstring("Command History", "Select a command:", parent=window, menu=history)
        if selected_item:
            command_entry_var.set(selected_item)

    # Save the reference to the command history menu
    window.command_history_menu = command_history_menu

    # Rebind KeyRelease event
    command_entry.bind("<KeyRelease>", handle_autocomplete)

# Function to set blurred background image
def set_blurred_background(window, image_path, blur_radius):
    # Blur the image
    original_image = Image.open(image_path)
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))

    # Convert the PIL Image to a Tkinter PhotoImage
    tk_blurred_image = ImageTk.PhotoImage(blurred_image)

    # Create a label with the blurred image as the background
    background_label = tk.Label(window, image=tk_blurred_image)
    background_label.image = tk_blurred_image  # Save a reference to avoid garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Function to blur the image
def blur_image(image_path, blur_radius):
    original_image = Image.open(image_path)
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(blur_radius))
    return blurred_image

# Create the main window
window = tk.Tk()
window.title("GITS GUI")

# Set the image path and blur radius
image_path = "BG.png"
blur_radius = 5

# Set blurred background
set_blurred_background(window, image_path, blur_radius)

# Apply the 'clam' theme
style = ttk.Style()
style.theme_use('clam')

# Load a GITS logo (replace 'gits_logo.png' with your actual logo file)
logo_image = tk.PhotoImage(file='gits-logo.png').subsample(2, 2)
logo_label = tk.Label(window, image=logo_image)
logo_label.pack(pady=10)

# Create an entry for GITS commands with auto-complete
command_entry_var = tk.StringVar()
command_entry_placeholder = "Type your command here..."  # Placeholder text
command_entry = ttk.Entry(window, font=("Arial", 12), textvariable=command_entry_var, justify="left")
command_entry.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
# Insert the placeholder text
command_entry.insert(0, command_entry_placeholder)

# Set the background color to match the image
command_entry.configure(background="#F0F0F0")

# Bind events for auto-complete and placeholder handling
command_entry.bind("<KeyRelease>", handle_autocomplete)
command_entry.bind("<FocusIn>", lambda event: handle_focus_in(event, command_entry_placeholder))

# Create a button to execute commands with a nice style
execute_button = tk.Button(window, text="Execute GITS Command", command=execute_gits_command, font=("Arial", 14), padx=10, pady=10)
execute_button.pack(pady=10)

# Create a button to show command history
command_history_button = tk.Menubutton(window, text="Command History", font=("Arial", 12))
command_history_button.pack(pady=5, padx=10, fill=tk.BOTH, expand=True)
command_history_menu = tk.Menu(command_history_button, tearoff=0)
for item in get_command_history():
    command_history_menu.add_command(label=item, command=lambda value=item: command_entry_var.set(value))
command_history_button['menu'] = command_history_menu

# Create a text widget to display the results with a border
result_text = tk.Text(window, height=10, width=60, font=("Arial", 12), relief="solid", borderwidth=2)
result_text.pack(padx=10, fill=tk.BOTH, expand=True)

# Configure a scrollbar for the text widget
scrollbar = ttk.Scrollbar(window, orient="vertical", command=result_text.yview)
result_text.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")


# Function to handle focus in and remove the placeholder text
def handle_focus_in(event, placeholder_text):
    current_text = command_entry_var.get()
    if current_text == placeholder_text:
        command_entry_var.set("")


# Run the GUI
window.mainloop()
