def fib(n):
    return 1 if n == 1 or n == 2 else fib(n - 1) + fib(n - 2)


def main():
    n = int(input())
    i = 1
    while True:
        if fib(i) == n:
            print(i)
            break
        elif fib(i) > n:
            print(-1)
            break
        i += 1


if __name__ == '__main__':
    main()
