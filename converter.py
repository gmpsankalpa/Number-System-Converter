import tkinter as tk
from tkinter import ttk

def convert_number():
    input_number = entry_number.get()
    selected_option = combo_choices.get()

    try:
        if selected_option == "Decimal to Binary":
            result = bin(int(input_number))[2:]
        elif selected_option == "Decimal to Octal":
            result = oct(int(input_number))[2:]
        elif selected_option == "Decimal to Hexadecimal":
            result = hex(int(input_number))[2:]
        elif selected_option == "Binary to Decimal":
            result = str(int(input_number, 2))
        elif selected_option == "Octal to Decimal":
            result = str(int(input_number, 8))
        elif selected_option == "Hexadecimal to Decimal":
            result = str(int(input_number, 16))
        else:
            result = "Invalid choice"

        label_result.config(text=f"Result: {result}")

        # Add the conversion to the history listbox
        history_listbox.insert(0, f"{selected_option}: {input_number} -> {result}")

    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Number System Converter")

# Set the theme color
root.configure(bg='#3498db')  # Blue color

# Create and configure widgets with theme color
style = ttk.Style()
style.configure('TLabel', background='#3498db', foreground='white')
style.configure('TButton', background='#2980b9', foreground='white')
style.configure('TEntry', fieldbackground='#ecf0f1')

label_instruction = ttk.Label(root, text="Enter a number and choose a conversion:")
label_instruction.grid(row=0, column=0, columnspan=2, pady=10)

entry_number = ttk.Entry(root, width=20)
entry_number.grid(row=1, column=0, pady=5)

combo_choices = ttk.Combobox(root, values=[
    "Decimal to Binary",
    "Decimal to Octal",
    "Decimal to Hexadecimal",
    "Binary to Decimal",
    "Octal to Decimal",
    "Hexadecimal to Decimal"
])
combo_choices.grid(row=1, column=1, pady=5)

button_convert = ttk.Button(root, text="Convert", command=convert_number)
button_convert.grid(row=2, column=0, columnspan=2, pady=10)

label_result = ttk.Label(root, text="Result: ")
label_result.grid(row=3, column=0, columnspan=2)

# Create a Listbox for conversion history
history_listbox = tk.Listbox(root, width=40, height=10)
history_listbox.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
