def get_num_words(file_contents):
    """
    Counts the number of words in the book text.
    """
    words = file_contents.split()

    return len(words)


def get_num_characters(file_contents):
    """
    Counts the number of characters in the book text.
    """
    characters = {}
    for char in file_contents.lower():
        if char == "\n":
            continue
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters


def sort_characters(num_characters):
    """
    Sorts the characters by their count in descending order.
    """
    sorted_characters = []
    for key, value in num_characters.items():
        if key == "\n":
            continue
        if not key.isalpha():
            continue
        sorted_characters.append({"name": key, "num": value})

    # print(sorted_characters)
    # return sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
