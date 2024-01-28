def main():
    book_path = "books/frankenstein.txt"
    book_text = open_book(book_path)
    char_dict = get_character_count(book_text)
    word_count = get_word_count(book_text)
    create_report(book_path, word_count, char_dict)


def get_word_count(book):
    return len(book.split())


def get_character_count(book):
    char_dict = {}
    for c in book:
        char = c.lower()
        if not char in char_dict.keys():
            char_dict[char] = 1
            continue
        char_dict[char] += 1
    
    return char_dict
        
def create_report(book_path, word_count, char_dict):
    print(f"--- Begin report of {book_path}  ---")
    print(f"{word_count} words found in the document")
    print()

    char_list = []
    for k, v in char_dict.items():
        if k.isalpha():
            char_list.append((v, k))
        
    char_list.sort(reverse=True)

    for item in char_list:
        print(f"The'{item[1]} character appears {item[0]} times in the document")

    print("--- End report ---")


def open_book(book_path):
    with open(book_path) as f:
        return f.read()

main()