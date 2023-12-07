from collections import Counter

shoes_num = int(input())
shoes = map(int, input().split(' '))
customers = int(input())

shoes_counter = Counter(shoes)

sum = 0
while True:
    try:
        size, price = map(int, input().split(' '))

        if shoes_counter[size] != 0:
            shoes_counter[size] = shoes_counter[size] - 1
            sum += price

    except:
        break

print(sum)
