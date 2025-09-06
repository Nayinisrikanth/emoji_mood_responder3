# emoji_mood_responder.py
import re

# Mood definitions: keywords, emoji and response message
MOODS = {
    'happy': {
        'keywords': ['happy', 'joy', 'glad', 'good', 'great', 'fine'],
        'emoji': '😊',
        'message': "That's great to hear!"
    },
    'sad': {
        'keywords': ['sad', 'unhappy', 'down', 'depressed', 'blue'],
        'emoji': '😔',
        'message': "Cheer up! Here's a hug 🤗"
    },
    'angry': {
        'keywords': ['angry', 'mad', 'furious', 'irate'],
        'emoji': '😡',
        'message': "Take a deep breath 😤"
    },
    'tired': {
        'keywords': ['tired', 'sleepy', 'exhausted', 'fatigued'],
        'emoji': '😴',
        'message': "Rest well! 😌"
    },
    'excited': {
        'keywords': ['excited', 'thrilled', 'pumped', 'stoked', 'awesome'],
        'emoji': '🥳',
        'message': "Let's celebrate! 🎉"
    }
}

# Build a quick keyword -> mood lookup for detection
keyword_to_mood = {}
for mood, info in MOODS.items():
    for kw in info['keywords']:
        keyword_to_mood[kw] = mood

def detect_mood(text: str):
    """
    Detect mood by exact word match first (word boundaries).
    Falls back to substring check if nothing exact found.
    Returns mood key or None.
    """
    text = text.lower()
    # Extract words using regex to avoid punctuation issues
    words = re.findall(r'\b\w+\b', text)
    for w in words:
        if w in keyword_to_mood:
            return keyword_to_mood[w]
    # Secondary pass: check if any keyword appears as substring
    for kw, mood in keyword_to_mood.items():
        if kw in text:
            return mood
    return None

def respond_to_mood(mood: str):
    info = MOODS.get(mood)
    if info:
        print(f"{info['emoji']}  {info['message']}")
    else:
        print("I couldn't detect your mood. Try words like 'happy', 'sad', 'tired', 'excited' or 'angry'.")

def main():
    print("Hi — I'm your Emoji Mood Responder! (type 'exit' or 'quit' to stop)\n")
    while True:
        user = input("How are you feeling today? ").strip()
        if user == "":
            print("Please type something or 'exit' to quit.")
            continue
        if user.lower() in ('exit', 'quit'):
            print("Take care! Bye 👋")
            break
        mood = detect_mood(user)
        if mood:
            respond_to_mood(mood)
        else:
            print("Hmm, I couldn't quite detect the mood. Could you try another sentence (e.g., 'I'm happy' or 'feeling tired')?")

if __name__ == "__main__":
    main()