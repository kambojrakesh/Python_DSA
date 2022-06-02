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
            print(node)
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

if __name__=="__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai1"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    print(routes)
    route_graph = Graph(routes)

    sp = route_graph.get_path("Mumbai","New York")
    print(sp)