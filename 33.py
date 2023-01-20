def list_sort_check(lst):
    print(lst)
    if lst == sorted(lst):
        return 1
    elif lst == sorted(lst)[::-1]:
        return -1
    return 0

print(list_sort_check([3,2,1,4]))
        