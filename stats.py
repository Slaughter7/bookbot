from collections import Counter             #imports function from python module


def number_of_words(text):
    words = text.split()                    #uses "split" to split all of the words that were read in the file in the "get_book_text" function, into a list of individual words
    return len(words)                       #returns the length of the list as an integer


def count_characters(text):
    character_count = Counter(text.lower()) #counts each instance of a letter in the provided text, after converting to lower case
    return dict(character_count)            #converts counter to a plain dictionary
    
def get_chars_dict(text):                   #boot.dev solution. More correct for the lesson. Checks if a letter is in the empty dictionary, and adds 1 if yes, sets to 1 if no.
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars