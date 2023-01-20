def enc(s):
    w = ""
    for i in s:
        if i == 'z':
            asc = 'a'
            w = w + asc
        elif i.isspace():
            continue
        else:
            asc = ord(i) + 1
            w = w + chr(asc)
    return w

def dec(d):
    w = ""
    for i in d:
        if i == 'a':
            w = w + 'z'
        else:
            w = w + chr(ord(i)-1)
    return w

x = input("")
print(enc(x))
print(dec(enc(x)))
