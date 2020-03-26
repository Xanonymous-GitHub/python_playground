def reader():
    data = input()
    if data == '0':
        return data
    return data + '\n' + reader()


def main():
    for i in range(len(data := reader()) - 1, -1, -1):
        print(data[i], sep='', end='')


if __name__ == '__main__':
    main()
