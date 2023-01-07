with open("books/frankenstein.txt") as f:
    contents = f.read()

def main():
    num_words = wd_ct(contents)
    print(f"There are {num_words} words found in the document.")

#print(letter_count(contents))

    keys_list = list(letter_count(contents))
    values_list = list(letter_count(contents).items())
    #print(f" I am {values_list[0]}")
    print(f"{letter_count(contents)}")
    

def wd_ct(words):
    count = len(words.split())
    return count

def letter_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()