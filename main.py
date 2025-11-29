from stats import number_of_words           #imports functions from other files in directory
from stats import count_characters

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)              #sets variable "text" to call the function "get_book_text" with input "path"
    word_count = number_of_words(text)      #sets variable "word_count" to call the function "number_of_words" with input "text"
    character_count = count_characters(text)
    print(f"Found {word_count} total words")
    print(character_count)


def get_book_text(path):
    with open(path) as f:                   #uses "open()" to open the path to our file, then returns the text that was in the file
        return f.read()


main()