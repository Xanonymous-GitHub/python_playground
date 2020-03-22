def main():
    n, m = list(map(int, input().split()))
    print((gcd := lambda _m, _n: _m if _n == 0 else gcd(_n, _m % _n))(m, n))


if __name__ == '__main__':
    main()
