# itertools-product
> <https://www.hackerrank.com/challenges/itertools-product/>

# solution

```python
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

```

* Python 라이브러리인 itertools를 활용하는 예제이다.
* `try-except` 문으로 `input()`을 받고, 해당 `input`값들을 `map(int, s.split(' '))`을 통해 int 형태의 데이터로 사용할 수 있게 했다.