# Exercise 51: Word Counter & Frequency
# Objective: Practice string manipulation, dictionary mapping, and clean text processing.

def text_analyzing(text: str):
    cleaned_text = text.lower()
    words = cleaned_text.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


print(text_analyzing("Python is great and Python is fun"))
