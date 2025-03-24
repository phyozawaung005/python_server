import tkinter as tk

class CounterApp:
    def __init__(self, master):
        self.master = master
        self.counter = 0

        self.label = tk.Label(master, text="Counter: 0", font=("Helvetica", 24))
        self.label.pack()

        self.increment_button = tk.Button(master, text="Increment", command=self.increment_counter)
        self.increment_button.pack()

        self.decrement_button = tk.Button(master, text="Decrement", command=self.decrement_counter)
        self.decrement_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_counter)
        self.reset_button.pack()

    def increment_counter(self):
        self.counter += 1
        self.update_counter_label()

    def decrement_counter(self):
        if self.counter > 0:
            self.counter -= 1
            self.update_counter_label()

    def reset_counter(self):
        self.counter = 0
        self.update_counter_label()

    def update_counter_label(self):
        self.label.config(text=f"Counter: {self.counter}")


def main():
    root = tk.Tk()
    root.title("Counter App")
    app = CounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
