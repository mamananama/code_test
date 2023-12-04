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
