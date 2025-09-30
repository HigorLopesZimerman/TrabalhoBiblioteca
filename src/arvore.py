class Arvore:
    def __init__(self, key, pos):
        self.key = key
        self.pos = pos
        self.left = None
        self.right = None
        
        
        
    def insert(self, key, pos):
        if key < self.key:
            if self.left is None:
                self.left = Arvore(key, pos)
            else:
                self.left.insert(key, pos)
        elif key > self.key:
            if self.right is None:
                self.right = Arvore(key, pos)
            else:
                self.right.insert(key, pos)
        else:
            # Se a chave já existe, atualiza a posição
            self.pos = pos
            
    
    def search(self, key):
        if key == self.key:
            return self.pos
        elif key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.search(key)
        else:
            if self.right is None:
                return None
            else:
                return self.right.search(key)
    
    
    def list_items(self):
        items = []
        if self.left:
            items += self.left.list_items()
        items.append((self.key, self.pos))
        if self.right:
            items += self.right.list_items()
        return f"\n{items}"      
    
    
    @staticmethod
    def build_tree(elements):
        root = None
        for key, pos in elements:
            if root is None:
                root = Arvore(key, pos)
            else:
                root.insert(key, pos)
        return root
        
    
    def inorder(self):
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append((self.key, self.pos))
        if self.right:
            elements += self.right.inorder()
        return elements
    
    
        
        
        
    
 #teste
if __name__ == "__main__":
    
    elements = [(67, 'receba'), (69, 'pereca'), (4, 'casa'), (3, 'bola'), (5, 'gato')]
    
    tree = Arvore.build_tree(elements)
    
    
    print(elements)
    
    print("Inorder traversal:", tree.inorder())
    print("Search for key 4:", tree.search(4))
    print("Search for key 6:", tree.search(67))
    print("List items:", tree.list_items())
    