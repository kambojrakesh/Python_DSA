class Tree:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()



def build_product_tree():
    root = Tree("Electronic")

    child1 = Tree("Laptop")
    child2 = Tree("Phone")

    root.add_child(child1)
    root.add_child(child2)

    #print("Hello")
    root.print_tree()

if __name__ == "__main__":
    build_product_tree()
