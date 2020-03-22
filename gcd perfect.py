def main():
    n, m = list(map(int, input().split()))
    print((gcd := lambda _m, _n: _m if not _n else gcd(_n, _m % _n))(m, n))


if __name__ == '__main__':
    main()
