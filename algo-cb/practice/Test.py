class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
    
    def add_child(self, l):
        if self.parent == None:
            self.parent = l
            return
        
            
        if l < self.parent:
            if self.left is not None:
                self.left.left = l
                self.add_child(l)
            else:
                self.left = l
        else:
            if self.right is not None:
                self.right.right = l
                self.add_child(l)
            else:
                self.right = l
        
def create_tree(ls):
    t = Tree()
    
    for l in ls:
        t.add_child(l)
        
        
if __name__ == "__main__":
    ls = [12, 3,4,5,61,1]
    create_tree(ls)
