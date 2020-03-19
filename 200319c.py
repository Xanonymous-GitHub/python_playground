def my_bin(data):
    result = bin(data).replace("0b", "")
    length = len(result)
    if length < 4:
        result = "0" * (4 - length) + result
    return result


def main():
    data_pack = [int(data, 2) for data in input().split(",")]
    result = list()
    for data in data_pack:
        if not data % 5:
            result.append(data)
    print(','.join(map(my_bin, result)))


if __name__ == '__main__':
    main()
