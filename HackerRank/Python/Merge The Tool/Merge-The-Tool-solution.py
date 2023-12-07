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
