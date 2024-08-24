book_path = "books/frankenstein.txt"

def main():
    book_content = get_book_text(book_path)
    words = count_words(book_content)
    chars = count_chars(book_content)
    list_of_letters = []
    for char in chars:
        if char.isalpha():
            temp_dict = {}
            temp_dict["letter"] = char
            temp_dict["num"] = chars[char]
            list_of_letters.append(temp_dict)
    list_of_letters.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"Number of words in the book: {words}")
    print()
    for item in list_of_letters:
        print(f'The \'{item["letter"]}\' character was found {item["num"]} times')

def sort_on(dict):
    return dict["num"]

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

main()
