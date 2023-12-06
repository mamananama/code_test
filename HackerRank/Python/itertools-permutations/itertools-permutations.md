# itertools permutations
> <https://www.hackerrank.com/challenges/itertools-permutations/>

# solution
```python
from itertools import permutations

data = input().split(' ')

if len(data) > 1:
    result = list(map(lambda x: ''.join(
        x), permutations(data[0], int(data[1]))))
else:
    result = list(map(lambda x: ''.join(x), permutations(data[0])))

for i in sorted(result):
    print(i)
```

* Python 라이브러리인 itertools를 활용하는 예제이다.
* `data = input().split(' ')` 으로 `input`값들을 받고, 만약 input값 중 순열의 조합 수를 나타내는 숫자 값이 들어올 경우를 `if`문을 통해 처리하도록 했다.
* `.sort()`는 아무런 return 없이 iterable한 객체의 순서를 정렬하는 것이고, `sorted`는 iterable 가능한 객체의 순서를 정렬한 별도의 새로운 객체를 만들어낸다.