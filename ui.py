import tkinter as tk

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