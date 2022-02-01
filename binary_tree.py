# each individual node

from re import I


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root

        while temp is not None:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def delete(self, value):

        def delete_node(node, value):
            if node is None:
                return node

            if value < node.value:
                node.left = delete_node(node.left, value)
            elif value > node.value:
                node.right = delete_node(node.right, value)
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp

                if node.right is None:
                    temp = node.left
                    node = None
                    return temp

                temp = self.min_value_node(node.right)
                node.value = temp.value

                node.right = delete_node(node.right, value)

            return node

        delete_node(self.root, value)

    def min_value_node(self, current_node):

        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    def max_value_node(self, current_node):

        while current_node.right is not None:
            current_node = current_node.right

        return current_node

    # traverse each layer until child node
    def breadth_first_search(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return results

    # traverse parent then left subtree first and then right subtree
    def depth_first_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)

        return results

    # traverse left subtree, right subtree and parent
    def depth_first_post_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)

        traverse(self.root)

        return results

    # traverse left subtree, parent and then right subtree
    def depth_first_inorder(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)

        return results

    def print_tree(self):
        # print the tree vertically

        def print_binary_tree(node, space, height):
            if node is None:
                return
            space += height
            print_binary_tree(node.right, space, height)

            #print(' ' * height)
            print(' ' * space + str(node.value))

            print_binary_tree(node.left, space, height)

        print_binary_tree(self.root, 0, 5)

    def trim_tree(self, min_value, max_value):
        # trim the node and only keep node between min and max value

        def trim(node, min_value, max_value):
            if not node:
                return
            node.left = trim(node.left, min_value, max_value)
            node.right = trim(node.right, min_value, max_value)

            if min_value <= node.value <= max_value:
                return node

            if node.value < min_value:
                return node.right

            if node.value > max_value:
                return node.left

        trim(self.root, min_value, max_value)


my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(76)
my_tree.insert(52)
my_tree.insert(82)
my_tree.insert(76)
my_tree.insert(92)
my_tree.insert(41)
my_tree.insert(31)

print(my_tree.root)
print(my_tree.root.left)
print(my_tree.root.right)

print(my_tree.contains(18))

print('min value in tree: {}'.format(my_tree.min_value_node(my_tree.root)))

print('max value in tree: {}'.format(my_tree.max_value_node(my_tree.root)))

print('breadth first search: {}'.format(my_tree.breadth_first_search()))
print('dfs-preorder: {}'.format(my_tree.depth_first_pre_order()))
print('dfs-postorder: {}'.format(my_tree.depth_first_post_order()))
print('dfs-inorder: {}'.format(my_tree.depth_first_inorder()))

print('printing tree:')
my_tree.print_tree()
my_tree.trim_tree(20, 90)
print('breadth first search after trim', my_tree.breadth_first_search())
my_tree.print_tree()

my_tree.delete(41)
print('breadth first search after delete 41', my_tree.breadth_first_search())
my_tree.print_tree()
