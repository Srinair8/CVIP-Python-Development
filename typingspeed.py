import time
import random
import tkinter as tk
from tkinter import messagebox

class ResultsDialog(tk.Toplevel):
    def __init__(self, master, typed_words, elapsed_time, speed, accuracy):
        super().__init__(master)
        self.title("Typing Speed Tester Results")

        result_message = (
            f"Typed words: {typed_words}\n"
            f"Time taken: {elapsed_time:.2f} seconds\n"
            f"Typing speed: {speed:.2f} words per minute\n"
            f"Accuracy: {accuracy:.2f}%"
        )

        result_label = tk.Label(self, text=result_message, font=("Helvetica", 14))
        result_label.pack(padx=20, pady=20)

        ok_button = tk.Button(self, text="OK", command=self.destroy)
        ok_button.pack(pady=10)

class TypingSpeedTesterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Tester")

        self.text_to_type = ""
        self.start_time = 0

        self.label = tk.Label(master, text="Welcome to Typing Speed Tester!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.text_display = tk.Label(master, text="", font=("Helvetica", 14))
        self.text_display.pack(pady=10)

        self.entry = tk.Entry(master, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Typing", command=self.start_typing)
        self.start_button.pack(pady=10)

        self.check_button = tk.Button(master, text="Check Speed", command=self.check_typing)
        self.check_button.pack(pady=10)

        self.change_text_button = tk.Button(master, text="Change Text", command=self.change_text)
        self.change_text_button.pack(pady=10)

        self.exit_button = tk.Button(master, text="Exit", command=self.exit_application)
        self.exit_button.pack(pady=10)

    def generate_random_text(self, word_count):
        words = [
            "the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog",
            "programming", "is", "fun", "and", "rewarding",
            "practice", "makes", "perfect",
            "python", "is", "a", "versatile", "language",
            "coding", "is", "like", "poetry",
            "this", "is", "a", "sample", "text", "with", "more", "words", "for", "typing",
            "the", "more", "you", "practice", "the", "better", "you", "become"
            "a", "journey", "of", "a", "thousand", "miles", "begins", "with", "a", "single", "step"
            "all", "that", "glitters", "is", "not", "gold",
            "to", "be", "or", "not", "to", "be", "that", "is", "the", "question",
            "in", "the", "middle","of", "difficulty", "lies", "opportunity"
            "happiness", "depends", "upon", "ourselves",
            "the", "best", "way", "to", "predict", "the", "future", "is", "to", "invent", "it",
            "the", "future", "belongs", "to", "those", "who", "believe", "in", "the", "beauty", "of", "their","dreams"
        ]
        return " ".join(random.sample(words, word_count))

    def start_typing(self):
        self.text_to_type = self.generate_random_text(word_count=15)  #change the word count as needed
        self.text_display.config(text=self.text_to_type)
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)

    def check_typing(self):
        end_time = time.time()
        typed_text = self.entry.get()

        typed_words = len(typed_text.split())
        speed = self.calculate_typing_speed(end_time, typed_words)

        # to check accuracy
        correct_chars = sum([1 for c1, c2 in zip(self.text_to_type, typed_text) if c1 == c2])
        accuracy = (correct_chars / len(self.text_to_type)) * 100

        #to  display improved results window
        ResultsDialog(self.master, typed_words, end_time - self.start_time, speed, accuracy)

        self.start_button.config(state=tk.NORMAL)

    def calculate_typing_speed(self, end_time, typed_words):
        elapsed_time = end_time - self.start_time
        minutes = elapsed_time / 60.0
        words_per_minute = typed_words / minutes
        return words_per_minute

    def change_text(self):
        self.text_to_type = self.generate_random_text(word_count=15)  # to change the word_count as needed
        self.text_display.config(text=self.text_to_type)

    def exit_application(self):
        self.master.destroy()  # close the Tkinter window

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTesterApp(root)
    root.mainloop()
