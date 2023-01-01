class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dic = {}
        for start, end in self.edges:
            if start in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start] = [end]

        print("Graph Dict:", self.graph_dic)

    def get_path(self, start, end, path =[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dic:
            return []

        paths = []
        for node in self.graph_dic[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path

        if start not in self.graph_dic:
            return None

        shortest_path = None
        for node in self.graph_dic[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) > len(shortest_path):
                        shortest_path = sp

        return shortest_path
if __name__=="__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    rout_graph = Graph(routes)
    #paths = rout_graph.get_path("Mumbai", "New York")
    shortest_path = rout_graph.get_shortest_path("Mumbai", "Toronto")
    print(shortest_path)




