def main():
    words = list(input())
    left, right = str(), str()
    for i in range(len(words)):
        if words[i] == 'h':
            left, words = ''.join(words[:i + 1]), words[i + 1:]
            break
    for i in range(len(words) - 1, -1, -1):
        if words[i] == 'h':
            right, words = ''.join(words[i:]), words[:i]
            break
    words = ''.join(words).replace("h", "H")
    print(left + words + right)


if __name__ == '__main__':
    main()
