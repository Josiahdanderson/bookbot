with open("books/frankenstein.txt") as f:
    contents = f.read()

def main():
    num_words = wd_ct(contents)
    print(f"There are {num_words} words found in the document.")

    #print(letter_count(contents))

    keys_list = list(letter_count(contents))
    values_list = list(letter_count(contents).items())
    print(f" I am {values_list[0]}")
    

def wd_ct(words):
    count = len(words.split())
    return count

def letter_count(words):
    lower = words.lower()
    num_letters = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }
    for word in lower:
        if word == "a":
            num_letters['a'] += 1
        if word == "b": 
            num_letters['b'] += 1
        if word == "c": 
            num_letters['c'] += 1
        if word == "d": 
            num_letters['d'] += 1
        if word == "e": 
            num_letters['e'] += 1
        if word == "f": 
            num_letters['f'] += 1
        if word == "g": 
            num_letters['g'] += 1
        if word == "h": 
            num_letters['h'] += 1
        if word == "i": 
            num_letters['i'] += 1
        if word == "j": 
            num_letters['j'] += 1
        if word == "k": 
            num_letters['k'] += 1
        if word == "l": 
            num_letters['l'] += 1
        if word == "m": 
            num_letters['m'] += 1
        if word == "n": 
            num_letters['n'] += 1
        if word == "o": 
            num_letters['o'] += 1
        if word == "p": 
            num_letters['p'] += 1
        if word == "q": 
            num_letters['q'] += 1
        if word == "r": 
            num_letters['r'] += 1
        if word == "s": 
            num_letters['s'] += 1
        if word == "t": 
            num_letters['t'] += 1
        if word == "u": 
            num_letters['u'] += 1
        if word == "v": 
            num_letters['v'] += 1
        if word == "w": 
            num_letters['w'] += 1
        if word == "x": 
            num_letters['x'] += 1
        if word == "y": 
            num_letters['y'] += 1
        if word == "z": 
            num_letters['z'] += 1
    return num_letters

main()