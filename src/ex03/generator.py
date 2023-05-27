import random


def generator(text: str, sep: str = ' ', option: str = None) -> str:
    """
    Splits the text according to sep value and yield the substrings.
    option precise if an action is performed to the substrings before it is yielded.
    """
    if not isinstance(text, str) or not isinstance(sep, str):
        print('ERROR')
        return None
    words = text.split(sep)
    if option is None:
        pass
    elif option == 'ordered':
        words.sort()
    elif option == 'shuffle':
        shuffled_words = []
        while words:
            shuffled_words.append(words.pop(random.randint(0, len(words) - 1)))
        words = shuffled_words
    elif option == 'unique':
        words = list(set(words))
    else:
        print('ERROR')
        return None
    for word in words:
        yield word


if __name__ == '__main__':
    print('---')
    t = 'Le Lorem Ipsum est simplement du faux texte.'
    for w in generator(t, sep=' '):
        print(w)
    print('---')
    for w in generator(t, sep=' ', option='shuffle'):
        print(w)
    print('---')
    for w in generator(t, sep=' ', option='ordered'):
        print(w)
    print('---')
    t = 'Lorem Ipsum Lorem Ipsum'
    for w in generator(t, sep=' ', option='unique'):
        print(w)
    print('---')
    for w in generator(t, sep=' ', option='foo'):
        print(w)
    print('---')
    t = 1.0
    for w in generator(t, sep='.'):
        print(w)
    print('---')
    print()
    print('--- 01.03.00 ---')
    txt = 'This is a simple string for a basic test. Very simple.'
    for elem in generator(txt, sep=' '):
        print(elem)
    print('---')
    for elem in generator(txt, sep='.'):
        print(elem)
    print('---')
    for elem in generator(txt, sep='i'):
        print(elem)
    print('---')
    for elem in generator(txt, sep='si'):
        print(elem)
    print('---')
