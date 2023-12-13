n,m = map(int,input("Введите N и M 1-ой матрицы: ").split())
n1,m1 = map(int,input("Введите N и M 2-ой матрицы: ").split())
e1 = [[0]*m]*n
e2 = [[0]*m1]*n1
e3 = [[0] * n for i in range(m1)]
if m == n1:
    for i in range(n):
        x = input("Введите строчку: ").split()
        if len(x) != m:
            print("Введена неправильная строка!")
            break
        e1[i] = list(map(int,x))
    print()
    for i in range(n1):
        x = input("Введите строчку: ").split()
        if len(x) != m1:
            print("Введена неправильная строка!")
            break
        e2[i] = list(map(int,x))
    for i in range(2):
        for j in range(2):
            for k in range(3):
                e3[i][j] += e1[i][k] * e2[k][j]
            print(e3[i][j], end=" ")
        print()
else:
    print("Матрицы не умножаются!")
    
