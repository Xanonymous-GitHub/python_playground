class Calculator:
    def __init__(self, user_input: str):
        self.__data: str = '+' + user_input

    def __calc(self, data: str) -> int:
        pos = 1
        number = str()
        while pos < len(data) and data[pos] not in ['+', '-']:
            number += data[pos]
            pos += 1
        return int(number) * (1 if data[0] == '+' else -1) + (
            self.__calc(data[len(number) + 1:]) if pos != len(data) else 0
        )

    def __str__(self):
        return str(self.__calc(self.__data))


def main():
    print(Calculator(input()))


if __name__ == '__main__':
    main()
