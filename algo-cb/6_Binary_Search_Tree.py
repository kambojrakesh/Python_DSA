class Tree:
    def __init__(self, data):
        self.parent = None
        self.children = []
        self.data = data

    def addd_children(self, child):
        child.parent = self
        self.children.append(child)

    def level(self):
        p = self.parent
        level = 0

        while p:
            p = p.parent
            level += 1

        return level

    def print_tree(self):
        spaces = " " * self.level() * 3
        prefix = spaces + "|---" if self.parent else ""
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()

def build_tree():
    root = Tree("Electronics")
    tv = Tree("TV")
    mobiles = Tree("Mobiles")

    root.addd_children(tv)
    root.addd_children(mobiles)

    root.print_tree()

if __name__=="__main__":
    build_tree()