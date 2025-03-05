from stats import count_words
from stats import count_characters
from stats import sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:  
        file_contents = f.read()
        return file_contents


def main():
    text = get_book_text(sys.argv[1])
    word_count = count_words(text)
    char_count = count_characters(text)
    sorted_count = sort_chars(char_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_count:
        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
    

main()


