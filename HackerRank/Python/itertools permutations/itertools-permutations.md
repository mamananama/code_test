# collections Counter
> <https://www.hackerrank.com/challenges/collections-counter/>

# solution
```python
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
```

* Python 라이브러리인 collections를 활용하는 예제이다.
* `Counter()`를 사용하면 dictionary 형태로 각 항목의 갯수를 나타낸다.
  * `{항목1: 갯수, 항목2: 갯수 ...}`