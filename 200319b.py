def main():
    data = list(map(int, input().split()))
    amount = list()
    last = data[0]
    tmp_amount = 0
    for x in data:
        if x == last:
            tmp_amount += 1
        else:
            amount.append(tmp_amount)
            tmp_amount = 1
        last = x
    print(max(amount))


if __name__ == '__main__':
    main()
