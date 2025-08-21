import os

MARKER = ",,0000,0000,0000,,"

# Gets the path to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Gets the name of all subtitle files in the current directory
subtitle_files = sorted([f for f in os.listdir(current_dir) if f.lower().endswith((".ass", ".srt"))])

print("Found subtitle file(s):")
for filename in subtitle_files:
    print(f"- {filename}")

for filename in subtitle_files:

    processed_lines = []
    print(f"Processing {filename}...")

    # Reads the subtitle file into memory
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    # Handles dialogue based on file type
    if filename.lower().endswith(".ass"):

        for line in text.splitlines():

            # Filters out non-dialogue lines
            if line.startswith("Dialogue: "):

                # Removes the timing and styling data
                marker_index = line.find(MARKER)
                if marker_index != -1:
                    line = line[marker_index + len(MARKER):]

                # Removes the leading whitespace before any newline characters
                line = line.replace(" \\N", "\\n")

                # Removes unnecessary formatting
                line = line.replace("\\i1", "").replace("\\b1", "").replace("{}", "")

                # Saves the refined line
                processed_lines.append(line)
                print(line)

print("Execution complete.")