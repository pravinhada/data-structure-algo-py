class Vertex(object):

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, neighbor, weight=0):
        self.connected_to[neighbor] = weight

    def get_connection(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])


class Graph(object):

    def __init__(self):
        self.vert_list = {}
        self.num_of_vertices = 0

    def add_vertex(self, key):
        self.num_of_vertices += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def add_edge(self, from_vertex, to_vertex, cost=0):
        if from_vertex not in self.vert_list:
            nv = self.add_vertex(from_vertex)
        if to_vertex not in self.vert_list:
            nv = self.add_vertex(to_vertex)

        self.vert_list[from_vertex].add_neighbor(
            self.vert_list[to_vertex], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def __contains__(self, n):
        return n in self.vert_list


g = Graph()

for i in range(6):
    g.add_vertex(i)

g.add_edge(0, 1, 2)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 5)
g.add_edge(2, 3, 5)

for v in g:
    print(v)
