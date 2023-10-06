def print_rangoli(size):
    # your code goes here
    len_ = (size-1)*2 + 1

    for i in range(size-1):
        line = []
        s = ''
        for j in range(size-1):
            line.append(chr(ord('e')-j))
        line += line[:-1:-1]
        s = '-'.join(line)
        print(s.center(len_, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
