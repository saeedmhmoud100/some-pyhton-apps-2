

def get_words(file):
    words_list = ' '.join(open(file, 'r').readlines()).replace("\n", "").split()
    words_dict = {}

    for i in words_list:
        words_dict[i] = len(i)

    return words_dict


def show(n):
    myDict = get_words('1000_word.txt')
    new_dict = {}
    for (k, v) in myDict.items():
        if v == n:
            new_dict[k] = v
    print(new_dict)


show(8)
