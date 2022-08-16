def number(a, b, c, n1, n2, n3):
    
    i, j, k = 0, 0, 0

    while i < n1 and j < n2 and k < n3:

        if a[i] == b[j] and b[j] == c[k]:
            print(a[i]),
            i += 1
            j += 1
            k += 1

        elif a[i] < b[j]:
            i += 1

        elif b[j] < c[k]:
            j += 1

        else:
            k += 1


a = [10, 11, 12, 13, 14, 15]
b = [12, 13, 14, 15, 16]
c = [14, 15, 16, 17, 18]
n1 = len(a)
n2 = len(b)
n3 = len(c)
print(number(a, b, c, n1, n2, n3))
