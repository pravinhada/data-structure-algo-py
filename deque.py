class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)


deque = Deque()
deque.add_front(2)
deque.add_front(5)

print('size {}'.format(deque.size()))


deque.add_rear(1)

print('removed {}'.format(deque.remove_front()))
