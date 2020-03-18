def main():
    n = int(input())
    m = int() + n
    top, end = list(), list()
    for i in range(m, 1, -2):
        tmp = [" "] * n
        pos = int((n - i) / 2)
        tmp[pos] = "*"
        tmp[pos + i - 1] = "*"
        top.append(tmp)
        end.insert(0, tmp)
    for x in top:
        print(''.join(x))
    print(" " * int(n / 2) + "*")
    for y in end:
        print(''.join(y))


if __name__ == '__main__':
    main()
