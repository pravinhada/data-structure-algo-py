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

    def min_value_node(self, current_node):

        while current_node.left is not None:
            current_node = current_node.left

        return current_node

    def max_value_node(self, current_node):

        while current_node.right is not None:
            current_node = current_node.right

        return current_node

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


my_tree = BinarySearchTree()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(76)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.root)
print(my_tree.root.left)
print(my_tree.root.right)

print(my_tree.contains(18))

print(my_tree.min_value_node(my_tree.root))

print(my_tree.max_value_node(my_tree.root))

print('bfs', my_tree.breadth_first_search())
print('dfs-preorder', my_tree.depth_first_pre_order())
print('dfs-postorder', my_tree.depth_first_post_order())
print('dfs-inorder', my_tree.depth_first_inorder())
