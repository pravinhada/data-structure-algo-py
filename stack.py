class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    def is_empty(self):
        return self.height == 0

    def size(self):
        return self.height
    
    def peek(self):
        if self.height == 0:
            return None
        return self.top.value

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


stack = Stack(5)
stack.push(3)
stack.push(9)
stack.push(11)
stack.push(41)
stack.print_stack()

print('peek stack')
print(stack.peek())
print('pop stack:')
print(stack.pop())

stack.print_stack()

print('is empty {}'.format(stack.is_empty()))