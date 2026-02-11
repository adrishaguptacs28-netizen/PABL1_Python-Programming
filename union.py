a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

union = []

for num in a:
    if num not in union:
        union.append(num)

for num in b:
    if num not in union:
        union.append(num)

print(union)
