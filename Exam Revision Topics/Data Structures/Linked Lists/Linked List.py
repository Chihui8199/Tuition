class Node:
    def __init__(self, data):  # Initialize node
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def print_ll(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def remove_first_node(self):
        if self.head is None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_node(self, num):
        current = self.head
        if current and current.data == num:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != num:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None


llist = Linkedlist()

# add nodes to the linked list
llist.insert_at_end('a')
llist.insert_at_end('b')
llist.insert_at_begin('c')
llist.insert_at_end('d')

print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("\nLinked list after removing a node:")
llist.print_ll()

print("\nNode Data")
llist.print_ll()
