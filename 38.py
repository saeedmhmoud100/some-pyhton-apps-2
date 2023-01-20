def func(f):
    file = open(f, "r").read()
    lines = len(file) - len(''.join(file.split()))
    words = len(file.split())
    characters = len(''.join(file.split()))

    print('the numpers of lines: ', lines)
    print('the numpers of words: ', words)
    print('the numpers of characters: ', characters)


func('1.txt')
