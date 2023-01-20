def func(f1, f2):
    file1 = open(f1, "r")
    with open(f2, "w") as file2:
        file2.write(file1.read())


func('1.txt', '2.txt')
