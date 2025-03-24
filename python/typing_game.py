import tkinter as tk
from tkinter import messagebox
import random
import time

# List of words
word_list = ["abstraction", "algorithm", "bandwidth", "binary", "boolean", "buffer", "cache", "circuit", "cloud",
             "compile",
             "compute", "concurrency", "cryptography", "database", "debugging", "decryption", "defragment", "digital",
             "encryption", "firewall", "firmware", "gateway", "hardware", "heuristic", "hyperlink", "indexing",
             "inheritance",
             "input", "instance", "integer", "interface", "internet", "iteration", "kernel", "latency", "loop",
             "machine",
             "memory", "modularity", "multicast", "network", "node", "object", "operator", "packet", "parameter",
             "partition",
             "pointer", "port", "processor", "protocol", "queue", "recursion", "redundancy", "register", "resolution",
             "router", "scalar", "scheduler", "scripting", "semaphore", "socket", "software", "stack", "storage",
             "subnet",
             "syntax", "throughput", "topology", "transistor", "variable", "vector", "virtualization", "virus",
             "voltage",
             "web", "wireless", "workflow", "binary", "browser", "bug", "byte", "checksum", "codec", "compression",
             "daemon",
             "data", "debug", "default", "domain", "echo", "emulator", "export", "format", "frame", "function", "grid",
             "host", "index", "input"]


class TypingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Game")
        self.start_time = None

        self.word_to_type = random.choice(word_list)

        # Create UI elements
        self.label = tk.Label(root, text="Type the word:", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.word_label = tk.Label(root, text=self.word_to_type, font=("Helvetica", 20, "bold"))
        self.word_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 16))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.check_input)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again)
        self.play_again_button.pack(pady=10)
        self.play_again_button.config(state=tk.DISABLED)

    def check_input(self, event):
        user_input = self.entry.get().strip()
        if user_input == self.word_to_type:
            end_time = time.time()
            time_taken = end_time - self.start_time
            wpm = self.calculate_wpm(time_taken, len(self.word_to_type))
            self.result_label.config(
                text=f"Great! You typed the word correctly in {time_taken:.2f} seconds.\nYour typing speed is {wpm:.2f} WPM.")
            self.play_again_button.config(state=tk.NORMAL)
        else:
            self.result_label.config(text=f"Oops! That's not correct.\nThe correct word was: {self.word_to_type}")
            self.play_again_button.config(state=tk.NORMAL)

    def calculate_wpm(self, time_taken, word_length):
        return (word_length / 5) / (time_taken / 60)

    def play_again(self):
        self.word_to_type = random.choice(word_list)
        self.word_label.config(text=self.word_to_type)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)
        self.start_time = time.time()


# Initialize the application
root = tk.Tk()
app = TypingGameApp(root)
root.mainloop()
