from stats import get_num_words
from stats import get_character_use_count

def get_book_text(filepath):
    file_contents = filepath.read()
    get_num_words(file_contents)
    get_character_use_count(file_contents)



def main():
    with open("books/frankenstein.txt", "r", encoding ="utf-8") as f:
        get_book_text(f)
)


main()