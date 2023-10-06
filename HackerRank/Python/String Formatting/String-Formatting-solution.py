def print_formatted(number):
    # your code goes here
    format_width = len(bin(number)[2:])

    for i in range(1, number+1):
        dec_ = str(i)
        oct_ = oct(i)[2:].upper()
        hex_ = hex(i)[2:].upper()
        bin_ = bin(i)[2:]

        print(dec_.rjust(format_width), end="")
        print(oct_.rjust(format_width+1), end="")
        print(hex_.rjust(format_width+1), end="")
        print(bin_.rjust(format_width+1), end="")
        print('')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
