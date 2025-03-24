import tkinter as tk


class ConverterApp:
    def __init__(self, master):
        self.master = master

        self.temp_frame = tk.Frame(master)
        self.temp_frame.pack(pady=10)

        self.temp_label = tk.Label(self.temp_frame, text="Temperature Converter", font=("Helvetica", 16))
        self.temp_label.pack()

        self.temp_entry = tk.Entry(self.temp_frame, width=10)
        self.temp_entry.pack()

        self.temp_var = tk.StringVar()
        self.temp_var.set("Celsius")

        self.temp_menu = tk.OptionMenu(self.temp_frame, self.temp_var, "Celsius", "Fahrenheit")
        self.temp_menu.pack()

        self.convert_button = tk.Button(self.temp_frame, text="Convert", command=self.convert_temperature)
        self.convert_button.pack()

        self.result_label = tk.Label(self.temp_frame, text="", font=("Helvetica", 14))
        self.result_label.pack()

        self.length_frame = tk.Frame(master)
        self.length_frame.pack(pady=10)

        self.length_label = tk.Label(self.length_frame, text="Length Converter", font=("Helvetica", 16))
        self.length_label.pack()

        self.length_entry = tk.Entry(self.length_frame, width=10)
        self.length_entry.pack()

        self.length_var = tk.StringVar()
        self.length_var.set("Meters")

        self.length_menu = tk.OptionMenu(self.length_frame, self.length_var, "Meters", "Feet")

