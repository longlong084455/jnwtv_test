# coding:utf-8

a = ['1', '3', '5']
b = ['2', '4', '6', '7']
c = []
for i in range(len(a)):
    j = 0
    if i + j <= len(b) - 1:
        for j in range(len(b)):
            c.append(a[i])
            c.append(b[i+j])
            break
    else:
        c.append(a[i])

print c

