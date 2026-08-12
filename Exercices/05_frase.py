# In this exercise we analyze a user-provided sentence, count words, manipulate specific tokens, and mask characters.

phrase = input("Enter a phrase: ")
words = phrase.split()
print(f"Total words: {len(words)}")

first_word = words[0].upper()
last_word = words[-1].upper()
print(f"First word is: {first_word}")
print(f"Last word is: {last_word}")

masked_phrase = phrase.replace("a" , "*").replace("A" , "*")
print(f"Masked phrase: {masked_phrase}")
