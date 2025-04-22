import sys

from stats import get_num_characters, get_num_words, sort_characters


def get_book_text(path_to_file):
    """
    Reads a book from a file and returns its text.
    """
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


def sort_on(dict):
    return dict["num"]


def print_report(book_path, num_words, sorted_characters):
    """
    Prints a report of the number of words and characters in the book text.
    """
    formatted_sorted_list = []
    for character in sorted_characters:
        formatted_sorted_list.append(f"{character['name']}: {character['num']}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        print(f"{character['name']}: {character['num']}")


if __name__ == "__main__":
    # path_to_file = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    file_contents = get_book_text(path_to_file)
    number_of_words = get_num_words(file_contents)
    # print(f"{number_of_words} words found in the document")
    number_of_characters = get_num_characters(file_contents)
    # print(f"{number_of_characters}")
    sorted_characters = sort_characters(number_of_characters)
    sorted_characters.sort(key=sort_on, reverse=True)
    print_report(path_to_file, number_of_words, sorted_characters)
