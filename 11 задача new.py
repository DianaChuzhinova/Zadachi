string = input("Введите свои товарчики): ")
items = [item.strip() for item in string.split(',')]
count = {}
for item in items:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1
sort_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
print("Товар\tКоличество")
for item, quantity in sort_count:
    print(f"{item}\t\t{quantity}")
