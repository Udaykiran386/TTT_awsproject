import re
from collections import Counter


def count_words(text):
    """Normalizes case and punctuation, then returns word counts as a dictionary."""
    # Convert text to lowercase
    lower_text = text.lower()

    # Extract words using regex (matches sequence of alphanumeric characters)
    words = re.findall(r"\b\w+\b", lower_text)

    # Count occurrences and return as a standard dictionary
    return dict(Counter(words))


# Example usage
sample_text = "Hello, world! Hello World... Python is great, isn't it? Python rules!"
word_counts = count_words(sample_text)

print(word_counts)