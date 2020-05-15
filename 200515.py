class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_


class LinkedList:
    def __init__(self, data: str, _generic_type: type = int):
        self.head = Node()
        self.generic_type = _generic_type
        data_list = list(map(self.generic_type, data.split()))
        for element in data_list[::-1]:
            self.add_node_at_head(Node(element))

    def add_node_at_head(self, node: Node):
        if self.head.next is not None:
            node.next = self.head.next
        self.head.next = node

    def remove_specific_value(self, specific_value):
        specific_value = self.generic_type(specific_value)
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if current_node.data == specific_value:
                current_node = current_node.next
                previous_node.next = current_node
            else:
                previous_node = current_node
                current_node = current_node.next

    @property
    def __raw(self) -> list:
        result = list()
        current_node = self.head.next
        while current_node is not None:
            result.append(current_node.data)
            current_node = current_node.next
        return result

    def __str__(self):
        return ' '.join(map(str, self.__raw))

    __repr__ = __str__


def main():
    # create a new linked list object with data and (maybe) a specific data type (generic).
    # default type will be 'int', but we use 'str' here, that means our linked list is str type.
    linked_list = LinkedList(input(), str)

    # remove every matched value inside the linked list.
    # warring: notice the inputted data type is str, not exactly match to your linked list type.
    linked_list.remove_specific_value(input())

    # show the linked list.
    print(linked_list)


if __name__ == '__main__':
    main()
