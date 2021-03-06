class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_queue = Queue(4)

my_queue.enqueue(24)
my_queue.enqueue(7)

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.dequeue())
my_queue.print_queue()

print('size of queue {}'.format(my_queue.size()))