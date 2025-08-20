import os

current_dir = os.path.dirname(os.path.abspath(__file__))

subtitle_files = [
    f for f in os.listdir(current_dir)
    if f.lower().endswith((".ass", ".srt"))
]

print("Found subtitle file(s):")
for filename in subtitle_files:
    print(f"- {filename}")

for filename in subtitle_files:

    # Read the subtitle file into memory
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    print(f"Processing {filename}...")

    # Discover dialogue lines based on file type
    if filename.lower().endswith(".ass"):
        dialogue_lines = [line for line in text.splitlines() if line.startswith("Dialogue: ")]
    elif filename.lower().endswith(".srt"):
        pass # .srt line discovery logic would go here