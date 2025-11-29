from stats import number_of_words           #imports functions from other files in directory
from stats import count_characters
from stats import sort_dicts
import sys

def main():
    if len(sys.argv) != 2:                  #checks for an argument when running the application, making sure there are only 2 (the program itself and the path to the book)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)                         #if there aren't two arguments, then it exits with status code 1. If there are, then it continues to run the program
    path = sys.argv[1]
    text = get_book_text(path)              #sets variable "text" to call the function "get_book_text" with input "path"
    word_count = number_of_words(text)      #sets variable "word_count" to call the function "number_of_words" with input "text"
    character_count = count_characters(text)
    sorted_count = sort_dicts(character_count)
    print_report(path, word_count, sorted_count)    #calls the function print_report() with the three variables it needs to print 
    

def print_report(path, word_count, sorted_count):   #new function to handle the printing
    print("============ BOOKBOT ============")  #prints using the format bootdev is looking for
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_count:                      #checks each entry in the list to see if the "char" character is an alphabetical character, and skips ones that aren't
        if not i["char"].isalpha():
            continue
        print(f"{i['char']}: {i['num']}")       
    print("============= END ===============")
              


def get_book_text(path):
    with open(path) as f:                   #uses "open()" to open the path to our file, then returns the text that was in the file
        return f.read()


main()