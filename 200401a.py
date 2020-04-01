def get_pos(m, n, data):
    max_pos = data.index(max(list(set(data)))) + 1
    return int((max_pos / m) - 1), int((max_pos % n if max_pos % n else n) - 1)


def main():
    m, n = list(map(int, input().split()))
    data = list()
    for x in range(m):
        data += list(map(int, input().split()))
    print(' '.join(map(str, get_pos(m, n, data))))


if __name__ == '__main__':
    main()
