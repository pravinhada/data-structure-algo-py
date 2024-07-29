class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = self.length + 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev = self.get(index - 1)
            temp = prev.next
            prev.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def pop(self):
        if self.head == None:
            return None

        temp = self.head
        prev = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        prev = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = prev
            prev = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def size(self):
        return self.length

    def cycle_check(self):
        # check whether the linked list is cyclic

        marker1 = self.head
        marker2 = self.head

        while marker2 != None and marker2.next != None:
            marker1 = marker1.next
            marker2 = marker2.next.next

            if marker1 == marker2:
                return True

        return False

    def nth_to_last_node(self, n,):
        # find the Nth to the Last Node in Linked list

        left_pointer = self.head
        right_pointer = self.head

        for _ in range(n-1):
            if not right_pointer.next:
                raise LookupError('Error: n is larger than the linked list')

            right_pointer = right_pointer.next

        while right_pointer.next:
            left_pointer = left_pointer.next
            right_pointer = right_pointer.next

        return left_pointer


my_linked_list = LinkedList(4)
my_linked_list.append(25)
my_linked_list.append(32)
my_linked_list.append(8)
my_linked_list.print_list()
print('size of list is: ' + str(my_linked_list.size()))

print('node at index 2 is: {}'.format(my_linked_list.get(2)))

my_linked_list.set_value(2, 70)
my_linked_list.print_list()

my_linked_list.insert(2, 33)
my_linked_list.print_list()


my_linked_list.remove(4)
my_linked_list.print_list()

my_linked_list.reverse()
print('\n')
my_linked_list.print_list()


print('Is cyclic linked list? {}'.format(my_linked_list.cycle_check()))


print('nth to the last node of 3 is: {}'. format(
    my_linked_list.nth_to_last_node(2).value))
