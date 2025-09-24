class Arvore:
    def __init__(self, key, pos):
        self.key = key
        self.pos = pos
        self.right = None
        self.left = None
        
        
        
    
    def add_child(self, key, pos):
        if self.key == key:
            return
        
        if key < self.key:
            if self.left:
                self.left.add_child(key, pos)
            else:
                self.left = Arvore(key, pos)
        else:
            if self.right:
                self.right.add_child(key, pos)
            else:
                self.right = Arvore(key, pos)
        
    
    def build_tree(self, pos, key):
        ...
                         