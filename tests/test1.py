import customtkinter as ctk
from tkinter import StringVar
import calendar
from datetime import datetime


class DropdownDatePicker(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dropdown Date Picker")
        self.geometry("300x200")

        # Variables to store selected values
        self.selected_year = StringVar(value=str(datetime.now().year))
        self.selected_month = StringVar(value=str(datetime.now().month))
        self.selected_day = StringVar(value=str(datetime.now().day))

        # Layout for dropdowns
        self.label = ctk.CTkLabel(self, text="Select a Date:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.dropdown_frame = ctk.CTkFrame(self)
        self.dropdown_frame.pack(pady=10)

        # Year Dropdown
        years = [str(year) for year in range(datetime.now().year - 50, datetime.now().year + 51)]
        self.year_menu = ctk.CTkOptionMenu(self.dropdown_frame, values=years,
                                           variable=self.selected_year, command=self.update_days)
        self.year_menu.grid(row=0, column=0, padx=5, pady=5)

        # Month Dropdown
        months = [str(month) for month in range(1, 13)]
        self.month_menu = ctk.CTkOptionMenu(self.dropdown_frame, values=months,
                                            variable=self.selected_month, command=self.update_days)
        self.month_menu.grid(row=0, column=1, padx=5, pady=5)

        # Day Dropdown
        self.day_menu = ctk.CTkOptionMenu(self.dropdown_frame, values=self.get_days(),
                                          variable=self.selected_day)
        self.day_menu.grid(row=0, column=2, padx=5, pady=5)

        # Confirm Button
        self.confirm_button = ctk.CTkButton(self, text="Confirm", command=self.confirm_date)
        self.confirm_button.pack(pady=10)

    def get_days(self):
        """Get the days of the selected month and year."""
        year = int(self.selected_year.get())
        month = int(self.selected_month.get())
        num_days = calendar.monthrange(year, month)[1]
        return [str(day) for day in range(1, num_days + 1)]

    def update_days(self, *args):
        """Update the days in the day dropdown when year or month changes."""
        days = self.get_days()
        self.day_menu.configure(values=days)
        if self.selected_day.get() not in days:
            self.selected_day.set(days[0])  # Reset day to first if out of range

    def confirm_date(self):
        """Display the selected date."""
        year = self.selected_year.get()
        month = self.selected_month.get()
        day = self.selected_day.get()
        selected_date = f"{year}-{int(month):02d}-{int(day):02d}"
        ctk.CTkMessagebox.showinfo("Date Selected", f"Selected Date: {selected_date}")


if __name__ == "__main__":
    ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

    app = DropdownDatePicker()
    app.mainloop()