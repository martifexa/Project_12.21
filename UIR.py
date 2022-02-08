lst = [[1,2,3],[2,3],[9]]
for i in lst:
    if len(i)<5:
        i.append("5" *(5-len(i)))


print(lst)

