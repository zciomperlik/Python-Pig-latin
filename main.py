VOWELS = "aeiou"
PUNCTUATION = ".,?!"


def translate_word(word):
    """Convert a single word to Pig Latin, keeping trailing punctuation and numbers intact."""
    core = word.rstrip(PUNCTUATION)
    trailing = word[len(core):]

    # Leave empty fragments and anything containing digits untouched
    if not core or any(char.isdigit() for char in core):
        return word

    lower = core.lower()

    if lower[0] in VOWELS:
        result = lower + "yay"
    else:
        # Treat 'y' as a vowel only when the word has no other vowels (e.g. "rhythm")
        vowel_chars = VOWELS if any(char in VOWELS for char in lower) else VOWELS + "y"
        split = next((i for i, char in enumerate(lower) if char in vowel_chars), len(lower))
        result = lower[split:] + lower[:split] + "ay"

    return result + trailing


def to_pig_latin(text):
    """Convert a whole sentence, ignoring extra spaces."""
    return " ".join(translate_word(word) for word in text.split())


if __name__ == "__main__":
    text = input("Enter text to be converted into Pig Latin: ")
    result = to_pig_latin(text)
    # input() shows the result and holds the window open until Enter is pressed
    input(result + "\n\nPress Enter to close...")
