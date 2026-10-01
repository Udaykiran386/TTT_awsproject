import re
from collections import Counter

def count_words_safe(text):
    """
    Counts word frequencies in a text string.
    Safely rejects invalid inputs without crashing.
    """
    # 1. Handle None or empty inputs gracefully
    if text is None:
        return {}
    
    # 2. Reject non-string inputs (lists, numbers, dicts, etc.)
    if not isinstance(text, str):
        raise TypeError(f"Expected a string or None, but got {type(text).__name__}")

    # 3. Handle whitespace-only strings
    if not text.strip():
        return {}

    try:
        # Normalize case and extract words
        lower_text = text.lower()
        words = re.findall(r"\b\w+\b", lower_text)
        return dict(Counter(words))
    except Exception as e:
        # Safety net for unexpected runtime errors
        print(f"An unexpected error occurred during processing: {e}")
        return {}


# --- Examples / Testing Error Handling ---

# Valid string
print("1. Valid string:", count_words_safe("Hello world! Hello Python."))

# None input
print("2. None input:", count_words_safe(None))

# Whitespace input
print("3. Empty string:", count_words_safe("   "))

# Invalid input (Numeric or List) - handled via try-except block
try:
    count_words_safe(12345)
except TypeError as err:
    print(f"4. Handled bad input: {err}")