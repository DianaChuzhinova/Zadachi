x=input("Введите 1-ый список цифр через пробел: ").split(" ")
d=input("Введите 2-ой список цифр через пробел: ").split(" ")
e =[]
index1=0
index2=0
while index1 < len(x) and index2 < len(d):
    if d[index2]>=x[index1]:
        e.append(x[index1])
        index1 +=1
    else:
        e.append(d[index2])
        index2 +=1
if index1 < len(x):
    e += x[index1:]
if index2 < len(d):
    e += d[index2:]
print (e)
