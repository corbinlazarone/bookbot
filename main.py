import sys

from stats import number_of_words, number_of_characters, sort_dicts


def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    booke_path = sys.argv[1]
    booke_text = get_book_text(booke_path)
    num_words = number_of_words(booke_text)
    num_chars = number_of_characters(booke_text)
    sorted_chars = sort_dicts(num_chars)

    print("============ BOOKBOT ============")
    print("Analyzing a book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words.")
    print("---------- Character Count -------")
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("============= END ===============")


main()