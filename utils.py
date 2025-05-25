import re

def load_transcript(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def group_chunks_by_paragraphs(transcript, group_size=5):
    pattern = r"\[(\d{2}:\d{2} - \d{2}:\d{2})\]\s+(.*?)(?=\[\d{2}:\d{2} - |\Z)"
    matches = re.findall(pattern, transcript, re.DOTALL)

    grouped = []
    temp_text = []
    temp_times = []

    for idx, (timestamp, text) in enumerate(matches):
        text = ' '.join(text.strip().split())
        temp_times.append(timestamp)
        temp_text.append(text)

        if (idx + 1) % group_size == 0 or idx == len(matches) - 1:
            paragraph = ' '.join(temp_text)
            combined_time = f"{temp_times[0].split('-')[0]} - {temp_times[-1].split('-')[-1]}"
            grouped.append((combined_time, paragraph))
            temp_text = []
            temp_times = []

    return grouped
