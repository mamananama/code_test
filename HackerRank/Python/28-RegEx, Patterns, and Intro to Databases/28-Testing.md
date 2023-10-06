# Day 28: RegEx, Patterns, and Intro to Databases

https://www.hackerrank.com/challenges/30-regex-patterns/problem

#### Task

Consider a database table, Emails, which has the attributes First Name and Email ID. Given rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in .

#### Input Format

The first line contains an integer, , total number of rows in the table.
Each of the subsequent lines contains space-separated strings denoting a person's first name and email ID, respectively.

#### Constraints

- 2 <= N <= 30
- Each of the first names consists of lower case letters \[a-z\]only.
- Each of the email IDs consists of lower case letters \[a-z\], @and only.
- The length of the first name is no longer than 20.
- The length of the email ID is no longer than 50.

#### Output Format

Print an alphabetically-ordered list of first names for every user with a gmail account. Each name must be printed on a new line.

#### Sample Input

6

```
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
```

#### Sample Output

```
julia
julia
riya
samantha
tanya
```

### solution

```python
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())

    result = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        p = re.compile(r'@gmail.com')
        if re.search(p, emailID) != None:
            result.append(firstName)

    for i in sorted(result):
        print(i)

```

> 정규식을 사용하는 풀이
> 'gmail.com'을 사용하는 이메일을 찾아, first name을 알파벳 순서로 출력한다.
