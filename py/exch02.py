# Simple Text Analyzer
# This program analyzes a given text and provides statistics about it.

text = "Python is a great programming language. It is widely used in various fields such as web development, data science, and artificial intelligence."
# Count the number of characters in the text
num_characters = len(text)
print(f"Number of characters: {num_characters}") # Output: Number of characters: 123
# Count the number of words in the text
num_words = len(text.split())
print(f"Number of words: {num_words}") # Output: Number of words:
# Count the number of sentences in the text
num_sentences = text.count('.')
print(f"Number of sentences: {num_sentences}") # Output: Number of sentences: 2
# Count the frequency of each word in the text
word_frequency = {}
for word in text.split():
    word = word.strip('.,').lower() # Remove punctuation and convert to lowercase
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1