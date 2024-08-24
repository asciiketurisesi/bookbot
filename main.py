book_path = "books/frankenstein.txt"

def main():
    book_content = get_book_text(book_path)
    words = count_words(book_content)
    print(f"Number of words in the book: {words}")
    chars = count_chars(book_content)
    print(chars)

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
