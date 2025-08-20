import os

current_dir = os.path.dirname(os.path.abspath(__file__))

subtitle_files = [
    f for f in os.listdir(current_dir)
    if f.lower().endswith((".ass", ".srt"))
]

print("Found subtitle file(s):")
for filename in subtitle_files:
    print(f"- {filename}")