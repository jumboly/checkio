VOWELS = "aeiouy"

def translate(phrase):
    word = ""
    i = 0
    while i < len(phrase):
        word += phrase[i]
        if phrase[i] in VOWELS:
            i += 3
        elif phrase[i].isspace():
            i += 1
        else:
            i += 2
    return word

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
