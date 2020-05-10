def get_user_data(class_type: type) -> list:
    user_data = list(map(class_type, input().split()))
    return user_data


def sort_stack(stack: list) -> None:
    if len(stack) != 0:
        tmp = stack.pop()
        sort_stack(stack)
        insert_to_right_place(stack, tmp)


def insert_to_right_place(stack: list, element) -> None:
    if len(stack) != 0 and stack[-1] < element:
        tmp = stack.pop()
        insert_to_right_place(stack, element)
        stack.append(tmp)
        return
    stack.append(element)


def print_result(stack: list) -> None:
    print(' '.join(map(str, stack)))


def main():
    stack = get_user_data(int)
    sort_stack(stack)
    print_result(stack)


if __name__ == '__main__':
    main()
