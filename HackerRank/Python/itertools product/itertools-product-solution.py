from itertools import product

data = []
while True:
    try:
        s = input()
        data.append(map(int, s.split(' ')))
    except:
        break

result = product(*data)

for i in result:
    print(i, end=' ')
