def word_frequency(sentence):
    #We define a string punctuation containing the characters to be removed.
    punctuation = ".,!?;:'\"()[]{}"

    # Remove punctuation and convert to lowercase
    cleaned_sentence = "".join(char.lower() if char not in punctuation else ' ' for char in sentence)

    # Split the sentence into words and count their frequency
    word_counts = {}
    words = cleaned_sentence.split()
#return a dictionary where keys are unique words in the sentence, and values are the corresponding frequencies, ignoring punctuation and considering words in a case-insensitive manner.
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)