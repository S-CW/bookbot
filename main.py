def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_chars(text)
    chars_sorted_dict = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for char_dict in chars_sorted_dict:
        if char_dict["char"].isalpha():
            print(f"'{char_dict["char"]}' character was found {char_dict["num"]} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lowered_string = text.lower()
    chars = {}

    for c in lowered_string:
        chars[c] = chars.get(c, 0) + 1

    return chars

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(dict):
    sorted_list = []

    for key in dict:
        sorted_list.append({"char": key, "num": dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


main()