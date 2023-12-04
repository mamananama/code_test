# The Minion Game
<https://www.hackerrank.com/challenges/the-minion-game>

# Solution

```python
def minion_game(string):
    vowels = 'AEIOU'

    s = []
    k = []

    for i in range(len(string)):
        if string[i] not in vowels:
            s.append(i)
        else:
            k.append(i)

    stuart = 0
    kevin = 0

    for i in s:
        stuart += (len(string) - i)
    for i in k:
        kevin += (len(string) - i)

    if stuart > kevin:
        print(f'Stuart {stuart}')
    elif stuart < kevin:
        print(f'Kevin {kevin}')
    else:
        print('Draw')
```

* `vowels='AEIOU`를 선언하여 모음의 집합을 문자열로 표현, `if _ in vowels` 로 `string`의 모음을 따로 찾아낼 수 있도록 했다.
* 자음만 따로 모은, `s[]` 모음만 따로 모은, `k[]` 리스트를 선언했다.
* 해당 문자로 조합 가능한 문자열의 수는, `(해당 문자의 시작 index) - (문자열의 길이)`로 계산할 수 있다.
