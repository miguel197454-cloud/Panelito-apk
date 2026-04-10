import numpy as np
import re

# Tokenización simple (separa palabras ignorando signos)
def tokenize(sentence):
    return re.findall(r'\b\w+\b', sentence.lower())

# Stemmer básico (recorta sufijos comunes en español/inglés)
def stem(word):
    suffixes = [
        "ando", "iendo", "ción", "ciones", "mente", "idad", "idades",
        "ar", "er", "ir", "os", "as", "es", "s"
    ]
    
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[:-len(suffix)]
    
    return word

# Bag of Words
def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)

    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag