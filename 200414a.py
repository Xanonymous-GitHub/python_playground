def string_handler(words: str) -> str:
    length = len(words)
    pos = int(length / 2)
    left = words[:pos]
    right = words[pos + 1 if length % 2 else pos::][::-1]
    return "yes" if left == right else "no"


def main():
    while True:
        try:
            data = input()
            print(string_handler(data))
        except EOFError:
            break


if __name__ == '__main__':
    main()
