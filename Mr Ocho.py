import tkinter as tk

def replace_word_with_comma():
    input_text = input_textbox.get("1.0", "end-1c")
    lines = input_text.split("\n")

    output_lines = []
    for line in lines:
        words = line.split()
        updated_words = [word if word.lower() not in ['och', 'samt'] else ',' for word in words]
        updated_sentence = ' '.join(updated_words).replace(' ,', ',')
        output_lines.append(updated_sentence)

    output_textbox.delete("1.0", "end")
    output_textbox.insert("1.0", "\n".join(output_lines))


# Create the main window
window = tk.Tk()
window.title("Word Replacement")
window.geometry("400x300")

# Create input label and textbox
input_label = tk.Label(window, text="Enter sentences:")
input_label.pack()
input_textbox = tk.Text(window, height=5)
input_textbox.pack()

# Create button to process the input
process_button = tk.Button(window, text="Process", command=replace_word_with_comma)
process_button.pack()

# Create output label and textbox
output_label = tk.Label(window, text="Updated sentences:")
output_label.pack()
output_textbox = tk.Text(window, height=5)
output_textbox.pack()

# Start the GUI event loop
window.mainloop()
