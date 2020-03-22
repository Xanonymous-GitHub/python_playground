def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)


def main():
    n, m = list(map(int, input().split()))
    print(gcd(m, n))


if __name__ == '__main__':
    main()
