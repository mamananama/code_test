# Merge the Tools!
<https://www.hackerrank.com/challenges/merge-the-tools/>


# solution
```python
def merge_the_tools(string, k):
    t = []
    i = 0
    while i < len(string):
        t.append(string[i:i+k])
        i = i + k

    for i in t:
        temp = []
        for c in i:
            if c not in temp:
                temp.append(c)
        print(''.join(temp))
```

* `string`문자열이 주어지면, `k`의 단위로 문자열을 쪼갠뒤, 해당 문자열의 중복되는 문자를 제거하고 출력하는 문제이다.