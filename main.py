path = ""


def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents











def main():
    print(get_book_text("books/frankenstein.txt"))
    

main()