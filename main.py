def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)              #sets variable "text" to call the function "get_book_text" with input "path"
    word_count = number_of_words(text)      #sets variable "word_count" to call the function "number_of_words" with input "text"
    print(f"Found {word_count} total words")
    


def get_book_text(path):
    with open(path) as f:                   #uses "open()" to open the path to our file, then returns the text that was in the file
        return f.read()


def number_of_words(text):
    words = text.split()                    #uses "split" to split all of the words that were read in the file in the "get_book_text" function, into a list of individual words
    return len(words)                       #returns the length of the list as an integer
    






main()