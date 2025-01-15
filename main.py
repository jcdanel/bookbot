letters = {
        "a":0

        }

def count_words(input):
    split_text = input.split()
    count = 0

    for words in split_text:
        count += 1

    return count

def count_chars(input):
    input.lower()
    split_text = input.split()

    for word in split_text:
        for char in letters:
           if letters["a"] == char:
               letters["a"] += 1
         

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(count_chars(file_contents))
    print(letters)


main()
