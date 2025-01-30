class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def add_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


my_list = LinkedList()
assert len(my_list) == 0
assert my_list.head is None

my_list.add_node("Napoli")

assert len(my_list) == 1
assert my_list.head.data == "Napoli"

my_list.add_node("Milan")
assert len(my_list) == 2

assert [type(el) for el in my_list] == [Node,Node]