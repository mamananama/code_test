from itertools import permutations

data = input().split(' ')

if len(data) > 1:
    result = list(map(lambda x: ''.join(
        x), permutations(data[0], int(data[1]))))
else:
    result = list(map(lambda x: ''.join(x), permutations(data[0])))

for i in sorted(result):
    print(i)
