a = [[1,2,3],[4,[5,6]],7,[8,9]]

def gf(a):
    b = []
    for i in a:
        if type(i) == list:
            b += gf(i)
        else:
            b.append(i)
    return b
print(gf(a))
