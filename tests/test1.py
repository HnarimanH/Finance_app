import customtkinter as ctk

# Debug callback function
def on_selection(event):
    print(1)
    try:
        selected_item = combobox.get()  # Get the selected value
        print(f"Selected item: {selected_item}")
    except Exception as e:
        print(f"Error in selection: {e}")
        
# Main application
root = ctk.CTk()

# Debug: Ensure the app is initializing
print("App started.")

# Create a ComboBox
combobox = ctk.CTkComboBox(
    root,
    values=["Option 1", "Option 2", "Option 3"],  # List of options
    width=200,
    fg_color="lightblue",  # Optional: for customization
    command=on_selection(event=None )
)
combobox.set("Select an option")  # Default value
combobox.pack(pady=20)

# Debug: Ensure the ComboBox is created
print("ComboBox created.")

# Bind the event
combobox.bind("<<ComboboxSelected>>", on_selection)

# Debug: Confirm event binding
print("Event binding set.")

# Run the application
root.mainloop()