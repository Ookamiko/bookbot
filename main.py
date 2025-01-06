def split_words(text):
    return text.split()

def character_count(text):
    chars = {}
    for c in text.lower():
        if not(c in chars):
            chars[c] = 0

        chars[c] += 1

    return chars

def main():
    book_file = "books/frankenstein.txt"
    print(f"--- Begin report of {book_file} ---")
    with open(book_file) as f:
        file_contents = f.read()
        words = split_words(file_contents)
        chars = character_count(file_contents)
        print(f"{len(words)} words found in the document")
        print("")

        for c in chars:
            print(f"The '{c}' character was found {chars[c]} times")

    print('--- End report ---')

main()