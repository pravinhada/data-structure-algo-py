from enum import Enum
from collections import OrderedDict


class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3


class Node:

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = node and value = weight

    def __str__(self):
        return str(self.num)


class Graph:

    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, num):
        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight=0):

        if source not in self.nodes:
            self.add_node(source)

        if dest not in self.nodes:
            self.add_node(dest)

        self.nodes[source].adjacent[self.nodes[dest]] = weight


def depth_first_search(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            # set substraction set(['B', 'C']) - set('B')
            stack.extend(graph[vertex] - visited)

    return visited


def breadth_first_search(graph, start):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited


g = Graph()

g.add_edge(0, 1, 5)
g.add_edge(1, 2, 3)

print(g.nodes)

graph = {
    'A': set((['B', 'C'])),
    'B': set((['A', 'D', 'E'])),
    'C': set((['A', 'F'])),
    'D': set((['B'])),
    'E': set((['B', 'F'])),
    'F': set((['C', 'E'])),
}

print(depth_first_search(graph, 'A'))
print(breadth_first_search(graph, 'A'))
