def first_generator(word):
    """Creating a generator that reverses a word using a for loop"""
    for i in range(len(word) - 1, -1, -1):
        yield word[i]


def second_generator(word):
    """Creating a generator that doubles every character of a word"""
    return (character * 2 for character in word)


def third_generator(word='hello'):
    """Creating a generator that prints the characters of even index"""
    index = 0
    yield word[index]

    index += 2
    yield word[index]

    index += 2
    yield word[index]


