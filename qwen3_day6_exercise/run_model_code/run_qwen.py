import requests
import time
import os
from datetime import datetime

MODEL = "qwen3.5:0.8b"
BASE_URL = "http://localhost:11434/api/generate"

SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "prompts_and_responses.md")

def ask_model(prompt: str) -> tuple:
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant. Answer directly and concisely. Do not show your thinking process or internal reasoning. Just give the final answer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False,
        "options": {
            "temperature": 0.7,
            "num_predict": 1024
        },
        "think": False
    }
    start = time.time()
    response = requests.post(
        "http://localhost:11434/api/chat",  # chat endpoint, not generate
        json=payload
    )
    elapsed = round(time.time() - start, 2)

    data = response.json()
    result = data.get("message", {}).get("content", "").strip()
    if not result:
        result = "[No response returned by model]"

    return result, elapsed

def save_to_markdown(entries: list):
    grouped = {}
    for entry in entries:
        cat = entry["category"]
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(entry)

    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        f.write("# Prompt Evaluation — qwen3.5:0.8b\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("---\n\n")

        for category, cat_entries in grouped.items():
            f.write(f"# {category}\n\n")
            for i, entry in enumerate(cat_entries, 1):
                f.write(f"## Prompt {i}\n\n")
                f.write(f"**Prompt:**\n\n{entry['prompt']}\n\n")
                f.write(f"**Response:**\n\n{entry['response']}\n\n")
                f.write(f"**Response Time:** {entry['time']}s\n\n")
                f.write(f"**Notes:** {entry['notes']}\n\n")
                f.write("---\n\n")

    print(f"\n✅ Saved to {os.path.abspath(SAVE_PATH)}")

def load_existing_entries() -> list:
    """Fix 3: Load previous session entries from file on startup"""
    entries = []
    path = os.path.abspath(SAVE_PATH)
    if os.path.exists(path):
        print(f"📂 Found existing file — previous entries will be preserved.")
    return entries

CATEGORIES = [
    "Coding",
    "General Knowledge",
    "Reasoning",
    "Visual Question Answering"
]

print("=" * 60)
print("   Qwen3.5:0.8b — Manual Prompt Evaluation Tool")
print("=" * 60)
print("Type your prompt and press Enter.")
print("Commands:")
print("  /category  → switch category")
print("  /skip      → skip VQA or any prompt")
print("  /save      → save all results and exit")
print("  /quit      → exit without saving")
print("=" * 60)

print("\nAvailable categories:")
for i, cat in enumerate(CATEGORIES, 1):
    print(f"  {i}. {cat}")
choice = input("\nStart with category number: ").strip()
current_category = CATEGORIES[int(choice) - 1] if choice.isdigit() else CATEGORIES[0]
print(f"\n>>> Category set to: {current_category}\n")

entries = load_existing_entries()

while True:
    prompt = input(f"[{current_category}] Your prompt: ").strip()

    if prompt == "/quit":
        print("Exiting without saving.")
        break

    elif prompt == "/save":
        save_to_markdown(entries)
        break

    elif prompt == "/skip":
        note = input("Enter a note for why this was skipped: ").strip()
        entries.append({
            "category": current_category,
            "prompt": "Skipped",
            "response": "N/A",
            "time": "N/A",
            "notes": note
        })
        save_to_markdown(entries)
        print("Skipped and noted.\n")

    elif prompt == "/category":
        print("\nAvailable categories:")
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"  {i}. {cat}")
        choice = input("Select category number: ").strip()
        current_category = CATEGORIES[int(choice) - 1] if choice.isdigit() else current_category
        print(f">>> Category switched to: {current_category}\n")

    elif prompt == "":
        continue

    else:
        print("\n⏳ Waiting for model response...\n")
        response, elapsed = ask_model(prompt)
        print(f"MODEL: {response}")
        print(f"\n⏱ Response time: {elapsed}s")
        note = input("\nYour note (press Enter to skip): ").strip()
        entries.append({
            "category": current_category,
            "prompt": prompt,
            "response": response,
            "time": elapsed,
            "notes": note if note else "No notes added."
        })
        save_to_markdown(entries)
        print(f"✅ Auto-saved. ({len(entries)} entries so far)\n")