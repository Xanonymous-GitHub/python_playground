def main():
    data = list(map(int, input().split()))
    max_pos = data.index(max(data))
    min_pos = data.index(min(data))
    data[max_pos], data[min_pos] = data[min_pos], data[max_pos]
    print(' '.join(map(str, data)))


if __name__ == '__main__':
    main()
