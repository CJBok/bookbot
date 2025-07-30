from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_report(num_words, char_list, file):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in char_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")

    print("============= END ===============")
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = sys.argv[1]
    text = get_book_text(file)
    num_words = get_num_words(text)
    dict = get_char_dictionary(text)
    sorted_char_list = get_sorted_list(dict)

    print_report(num_words, sorted_char_list, file)

main()