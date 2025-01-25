import customtkinter as ctk
def create_ctk_window():
    # Sample data from the database
    Data = [
        (3000000, 'gaming keyboard', '1954-May-13'),
        (3, 'toy', '2017-April-2'),
        (1, 'toy', '1959-January-2'),
        (2, 'toy', '1955-January-4'),
        (3, 'toy', '1952-February-6'),
        (35000, 'nariman', '1950-January-1'),
        (300, 'nariman', '2022-February-3')
    ]
    # Initialize the customtkinter window
    ctk.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

    root = ctk.CTk()
    root.title("Database Viewer")
    root.geometry("500x400")

    # Create a scrollable frame for the data
    frame = ctk.CTkScrollableFrame(root, width=480, height=300)
    frame.grid(row=1, column=1)

    # Create column headers
    header_frame = ctk.CTkFrame(frame)
    header_frame.pack(fill="x", padx=5, pady=5)

    headers = ["Amount", "Description", "Date"]
    for idx, header in enumerate(headers):
        header_label = ctk.CTkLabel(header_frame, 
                            text=header, 
                            width=150, 
                            anchor="center", 
                            font=("Arial", 14, "bold"))
        header_label.grid(row=0, column=idx, padx=5, pady=5)

    # Display the data rows
    for row_idx, record in enumerate(Data):
        for col_idx, value in enumerate(record):
            label = ctk.CTkLabel(
                frame, text=str(value), width=150, anchor="center", font=("Arial", 12)
            )
            label.grid(row=row_idx + 1, column=col_idx, padx=5, pady=2)

    # Run the application
    root.mainloop()
# Call the function to create the window
create_ctk_window()