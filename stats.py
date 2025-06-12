def number_of_words(text):
    """
    Counts the number of words in a text.
    """
    words = text.split()
    return len(words)


def number_of_characters(text):
    """
    Counts the number of characters in a text.
    """
    char_dict = {}

    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha() or lower_char.isdigit():
            if lower_char in char_dict:
                char_dict[lower_char] += 1
            else:
                char_dict[lower_char] = 1
    return char_dict


def sort_dicts(dict):
    """
    Sorts a dictionary of characters and thier counts.
    """
    list_of_tuples = list(dict.items())
    list_of_tuples.sort(key=lambda x: x[1], reverse=True)
    return list_of_tuples