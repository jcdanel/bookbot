letters = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
        "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
        "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
        "y": 0, "z": 0
        }


def count_words(input):
    split_text = input.split()
    count = 0

    for words in split_text:
        count += 1

    return count

def count_chars(input):
    split_text = input.lower().split()

    for word in split_text:
        for char in word:
            for entry in letters:
                if entry == char:
                    letters[entry] += 1
    
    sorted_dict = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))

    for entry in sorted_dict:
        print(f"the {entry} character was found {letters[entry]} times")
           
         

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()


    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document\n")
    count_chars(file_contents)
    print("--- End report ---")


main()
