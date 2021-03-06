def comb(n, m):
    if m > n:
        return 0
    if m == n:
        return 1
    m = min(m, abs(m - n))
    if m == 1:
        return n
    return sum([comb(n - i - 1, m - 1) for i in range(n - m + 1)])


def main():
    data = list(map(int, input().split()))
    print(sum(comb(data.count(number), 2) for number in list(set(data))))


if __name__ == '__main__':
    main()
