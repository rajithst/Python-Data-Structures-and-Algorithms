from graph.linked_list import LinkedList


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        for i in vertices:
            self.adj_list[i] = LinkedList()

    def add_edge(self, from_node, to_node, directed=True):
        self.adj_list[from_node].insert_at_head(to_node)
        if not directed:
            self.adj_list[to_node].insert_at_head(from_node)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in self.vertices:
            print("|", i, end=" | => ")
            temp = self.adj_list[i].get_head()
            while temp is not None:
                print("[", temp.val, end=" ] -> ")
                temp = temp.next
            print("None")



