from tkinter import filedialog
import argostranslate.translate
import sys
import tkinter as tk

# Constants
FROM_CODE = "en"
TO_CODE = "pt"

# Global variables
filename = None
lines_header = None
lines_dialogue = None
line_counter = 0

# UI elements
root = None
text_input = None
button_frame = None
button_previous = None
button_play = None
button_next = None
text_output = None

# Button click event handlers
def on_button_previous_click():
    previous_line()

def on_button_play_click():
    play_line()

def on_button_next_click():
    next_line()

# Button action functions
def previous_line():

    global line_counter

    save_line()
    if line_counter == 0:
        return

    line_counter -= 1
    cycle_line()

def play_line():
    pass

def next_line():

    global line_counter

    save_line()
    if line_counter == len(filtered_lines) - 1:
        return
    
    line_counter += 1
    cycle_line()

def cycle_line():

    global filtered_lines, line_counter, text_input, text_output

    text_input.delete(1.0, tk.END)
    text_input.insert(tk.END, filtered_lines[line_counter])

    translated_line = argostranslate.translate.translate(filtered_lines[line_counter], FROM_CODE, TO_CODE)

    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, translated_line)

def initialize_ui():

    global root, text_input, button_frame, button_previous, button_play, button_next, text_output

    # Initialize the main application window
    root = tk.Tk()
    root.title("Subtitle Prompter")

    # Input text area
    text_input = tk.Text(root, height=4, width=60)
    text_input.pack(padx=10, pady=10)

    # Button frame
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    # Previous button
    button_previous = tk.Button(button_frame, text="Previous", width=8, command=on_button_previous_click)
    button_previous.pack(side=tk.LEFT, padx=5)

    # Play button
    button_play = tk.Button(button_frame, text="Play", width=8, command=on_button_play_click)
    button_play.pack(side=tk.LEFT, padx=5)

    # Next button
    button_next = tk.Button(button_frame, text="Next", width=8, command=on_button_next_click)
    button_next.pack(side=tk.LEFT, padx=5)

    # Output text area
    text_output = tk.Text(root, height=4, width=60)
    text_output.pack(padx=10, pady=10)

# Parses the subtitle file
def parse_subtitles(filename, file_content):

    # Handles dialogue based on file type
    if filename.lower().endswith(".ass"):

        lines_header = []
        lines_dialogue = []

        # Separates header and dialogue lines
        for line in file_content.splitlines():
            if line.startswith("Dialogue:"):
                lines_dialogue.append(parse_dialogue(line))
            else:
                lines_header.append(line)

        # Validates content
        if not lines_header or not lines_dialogue:
            print("Subtitle file is empty. Exiting...")
            sys.exit(1)

        cycle_line()

    else:
        print("Unsupported subtitle file format.")
        sys.exit(1)

# Separates metadata from dialogue and refines the dialogue line
def parse_dialogue(line):

    metadata_index = -1

    for i in range(9):
        metadata_index = line.find(",", metadata_index + 1)

    # Extracts the metadata
    metadata = line[:metadata_index+1]

    # Refines the line by removing unnecessary formatting
    line = line[metadata_index + 1:]
    line = line.replace(" \\N", "\\n")
    line = line.replace("\\i1", "").replace("\\b1", "").replace("{}", "")

    return [metadata, line, line]

