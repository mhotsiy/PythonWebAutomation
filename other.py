text = 'abccba'
print(text[1:-1])


def pallindrom(a):
    if len(a) <= 1:
        return True
    if a[0] != a[-1]:
        return False
    return pallindrom(a[1:-1])


print(pallindrom(text))

a = 'asd asd asd '
s1 = ''.join(a.split('6'))


print(len(s1).)


