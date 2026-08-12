# In this exercise we analyze string lengths, modify case formatting, and clean extra whitespace from user input.

phrase = input("Write a phrase about whatever you want: ")

original = print(f"The phrase that you wrote was: {phrase}")

phrase_striped = phrase.strip()
print(f"The phrase in uppercase is: {phrase_striped.upper()}")
print(f"The phrase in lowercase is: {phrase_striped.lower()}")
print(f"The phrase cleaned is: {phrase_striped}")
print(f"The amount of characters in the phrase without the spaces is: {len(phrase_striped.replace(' ', ''))}")
