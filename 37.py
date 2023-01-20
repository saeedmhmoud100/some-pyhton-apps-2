def func(f):
    with open(f, "r") as file:
        return file.read()[::-1]


print(func('1.txt'))
