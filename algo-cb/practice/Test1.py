class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dic = {}
        
        for route in self.edges:
            if route[0] in self.dic:
                self.dic[route[0]].append(route[1])
            else:
                self.dic[route[0]] = [route[1]]
        
    #self.dic: {'Mumbai': ['Paris', 'Dubai'], 'Paris': ['Dubai', 'New York'], 'Dubai': ['New York'], 'New York': ['Toronto']}
    def get_path(self, start, end, path =[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.dic:
            return []

        paths = []
        i = 0
        for node in self.dic[start]:
            #if node not in path:
            new_paths = self.get_path(node, end, path)
            paths.extend(new_paths)

        return paths
    
    
if __name__=="__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    
    #"Mumbai" : ["Paris", "Dubai"]
    rout_graph = Graph(routes)
    print(rout_graph.dic)
    paths = rout_graph.get_path("Mumbai", "New York")
    #shortest_path = rout_graph.get_shortest_path("Mumbai", "Toronto")
    print(paths)