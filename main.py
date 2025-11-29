from stats import number_of_words           #imports functions from other files in directory
from stats import count_characters
from stats import sort_dicts

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)              #sets variable "text" to call the function "get_book_text" with input "path"
    word_count = number_of_words(text)      #sets variable "word_count" to call the function "number_of_words" with input "text"
    character_count = count_characters(text)
    sorted_count = sort_dicts(character_count)
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