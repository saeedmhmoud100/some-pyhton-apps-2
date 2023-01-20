

def lists_check(lst1, lst2):
    check_items = 0
    lst1_len = 0
    lst2_len = 0
    for i in lst1:
        lst1_len += 1
    for i in lst2:
        lst2_len += 1

    for l1 in lst1:
        for l2 in lst2:
            if l1 == l2:
                check_items += 1
                break
    return 'lists are equal = ' + str(not (check_items < lst1_len or check_items < lst2_len))


print(lists_check([3,8, 1, 2, 5, 4], [1, 2, 3, 5, 4, 8]))
