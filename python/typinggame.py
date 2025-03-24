import random
import time

# List of words to be used in the game
word_list = ["networking", "python", "programming", "computer", "hardware", "software", "internet", "database",
             "algorithm", "security", "abstraction", "algorithm", "bandwidth", "binary", "boolean", "buffer", "cache", "circuit",
            "cloud", "compile", "compute", "concurrency", "cryptography", "database", "debugging",
            "decryption", "defragment", "digital", "encryption", "firewall", "firmware", "gateway",
            "hardware", "heuristic", "hyperlink", "indexing", "inheritance", "input", "instance",
            "integer", "interface", "internet", "iteration", "kernel", "latency", "loop", "machine",
            "memory", "modularity", "multicast", "network", "node", "object", "operator", "packet",
            "parameter", "partition", "pointer", "port", "processor", "protocol", "queue", "recursion",
            "redundancy", "register", "resolution", "router", "scalar", "scheduler", "scripting",
            "semaphore", "socket", "software", "stack", "storage", "subnet", "syntax", "throughput",
            "topology", "transistor", "variable", "vector", "virtualization", "virus", "voltage",
            "web", "wireless", "workflow", "binary", "browser", "bug", "byte", "checksum", "codec",
            "compression", "daemon", "data", "debug", "default", "domain", "echo", "emulator",
            "export", "format", "frame", "function", "grid", "host", "index", "input"
 ]


def calculate_wpm(time_taken, word_length):
    # WPM formula: (Number of characters / 5) / (Time in minutes)
    wpm = (word_length / 5) / (time_taken / 60)
    return wpm


def typing_game():
    print("Welcome to the Typing Game!")

    while True:
        # Choose a random word from the list
        word_to_type = random.choice(word_list)

        print(f"\nType this word: {word_to_type}")

        # Start the timer
        start_time = time.time()

        # Get user input
        user_input = input("Your input: ")

        # End the timer
        end_time = time.time()

        # Calculate the time taken
        time_taken = end_time - start_time

        # Check if the input matches the word
        if user_input == word_to_type:
            # Calculate WPM
            word_length = len(word_to_type)
            wpm = calculate_wpm(time_taken, word_length)
            print(f"Great! You typed the word correctly in {time_taken:.2f} seconds.")
            print(f"Your typing speed is {wpm:.2f} WPM.")
        else:
            print("Oops! That's not correct.")
            print(f"The correct word was: {word_to_type}")

        # Ask the player if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Game Over. Thanks for playing!")


# Run the game
typing_game()
