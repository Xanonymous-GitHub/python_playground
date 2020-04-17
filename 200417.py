def main():
    while True:
        try:
            print(''.join(list(chr(ord(word) - 7) for word in input())))
        except EOFError:
            break
    pass


if __name__ == '__main__':
    main()
