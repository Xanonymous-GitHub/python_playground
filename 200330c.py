def levels(n):
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result


def comb(n, m):
    if m > n:
        return 0
    if m == n:
        return 1
    m = min(m, abs(m - n))
    if m == 1:
        return n
    return int(levels(n) / (levels(m) * levels(n - m)))


def main():
    data = list(map(int, input().split()))
    print(sum(comb(data.count(number), 2) for number in list(set(data))))


if __name__ == '__main__':
    main()
