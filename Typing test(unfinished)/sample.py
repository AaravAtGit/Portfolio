import tkinter as tk
import time

def calculate_wpm(typing_time, num_words):
    return num_words / (typing_time / 60)

def calculate_accuracy(typed_words, actual_words):
    return (len(typed_words) - (len(actual_words) - len(typed_words))) / len(actual_words)

def submit():
    end_time = time.time()
    typing_time = end_time - start_time
    num_words = len(actual_words.split())
    wpm = calculate_wpm(typing_time, num_words)
    accuracy = calculate_accuracy(typed_text.get("1.0", "end"), actual_words) * 100
    result = "WPM: {:.2f}\nAccuracy: {:.2f}%".format(wpm, accuracy)
    result_label.config(text=result)

root = tk.Tk()
root.geometry("500x500")
root.title("Typing Test")

instructions = tk.Label(root, text="Type the following words:")
instructions.pack()

actual_words = "This is a typing test application"
actual_text = tk.Label(root, text=actual_words)
actual_text.pack()

typed_text = tk.Text(root, height=5, width=30)
typed_text.pack()

start_time = time.time()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
