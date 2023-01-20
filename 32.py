def lists_check(lst1, lst2):
    return (sorted(list(dict.fromkeys(lst1))) == sorted(list(dict.fromkeys(lst2))))


print(lists_check([1, 3, 2, 2], [2, 3, 1,5]))
