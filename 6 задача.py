x=input("Впишите строку: ")
d=x.split ( " " )
while "" in d:
    d.remove("")
d[0]= d[0].swapcase()
d[1]= d[1].swapcase()
d_count=len(d)
e=" ".join(d)
print(e, d_count)
