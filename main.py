from stats import get_num_words
from stats import get_character_use_count
from stats import dict_sort
import sys

def get_book_text(file_contents, filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    get_num_words(file_contents)
    print("--------- Character Count -------")
    get_character_use_count(file_contents)
    dict_sort(get_character_use_count(file_contents))
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    with open(filepath, 'r') as f:
        file_contents = f.read()
        # Rename the function to better reflect what it does
        get_book_text(file_contents, filepath)

main()