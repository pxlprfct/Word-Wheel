OPTIONAL = ['n', 'c', 'm', 'u', 'a', 'b', 'e', 'a']
REQUIRED = ['l']


def check_letters(string):
    """ Checks whether a word is ONLY made up from the valid letter set """
    string = string.strip()

    for let in string:
        # check each let(ter) of string against the lists
        if let not in OPTIONAL + REQUIRED:
            return False

    for let in REQUIRED:
        # check the WORD against REQUIRED
        if let not in string:
            return False
    return True


def print_longest(words):
    """ Prints the longest valid word, and how many letters is is made from """
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    print("The longest valid word was '{}' at {} letters long"
          .format(longest, len(longest)))


valid_words = []
# by using a set - we won't have duplicates - saving some time
for letter in set(OPTIONAL + REQUIRED):
    # only open + parse the dictionaries we need (as a slight time saving measure)
    f = open("./Dictionary/" + letter + ".txt", "r")

    for line in f:
        if check_letters(line):
            valid_words.append(line.strip())


valid_words.sort()

print("Optional Letters - {}\tRequired Letters - {}\n"
      .format(" ".join(OPTIONAL), " ".join(REQUIRED)))
print("With that letter set, there are {} valid words\n"
      .format(len(valid_words)))
print("\n".join(valid_words) + "\n")
print_longest(valid_words)
