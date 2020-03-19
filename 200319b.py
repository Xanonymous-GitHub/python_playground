def main():
    data = list(map(int, input().split()))
    items = list(set(data))
    amount = list()
    for item in items:
        amount.append(data.count(item))
    print(max(amount))


if __name__ == '__main__':
    main()
