def main():
    while True:
        n = input()
        m = len(n)
        if m % 2 == 0:
            if n[:m // 2] == n[m // 2:][::-1]:
                print("yes")
            else:
                print("no")
        else:
            if n[:(m // 2) + 1] == n[m // 2:][::-1]:
                print("yes")
            else:
                print("no")


if __name__ == '__main__':
    main()
