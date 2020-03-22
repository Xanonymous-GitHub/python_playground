class Converter:
    __syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    __val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    def __init__(self, data: int):
        self.__user_input = data

    def __convert(self) -> str:
        result = list()
        user_input = self.__user_input
        while True:
            current_number = -1
            for i, val in enumerate(self.__val):
                if val <= user_input:
                    current_number = i
                    break
            if current_number == -1:
                return ''.join(result)
            user_input -= self.__val[current_number]
            result.append(self.__syb[current_number])

    def __str__(self):
        return self.__convert()


def main():
    print(Converter(int(input())))


if __name__ == '__main__':
    main()
