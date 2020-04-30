class Node:
    def __init__(self, data=None, next_=None):
        self.data = data
        self.next = next_


class LinkedList:

    def __init__(self, node: Node = Node()):
        self.head = node

    def insert_on_head(self, element):
        if self.head.next is None:
            self.head.next = Node(element)
            return
        node = Node(element)
        node.next = self.head.next
        self.head.next = node

    def get_node_data(self, index_: int):
        current = self.head
        while index_:
            current = current.next
            index_ -= 1
        return current.data

    def add_with_sorted(self, element):
        previous = self.head
        current = self.head.next
        while current is not None and current.data <= element:
            previous = current
            current = current.next
        new_node = Node(element)
        new_node.next = current
        previous.next = new_node


def main():
    user_input = input().split()
    link_list_1 = LinkedList()
    for element in user_input[::-1]:
        link_list_1.add_with_sorted(element)
    index = int(input())
    print(link_list_1.get_node_data(index))


if __name__ == '__main__':
    main()
