def capitalize_words(sentence):
    """Return a list of uppercase words from the sentence."""
    # Split and convert each word to uppercase
    words = sentence.split()
    return [word.upper() for word in words]

def reverse_string(s):
    """Return the reverse of the provided string."""
    return s[::-1]

def word_count(sentence):
    """Return the number of words in the given sentence."""
    words = sentence.split()
    return len(words)