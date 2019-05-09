# left less, right greater
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while current.value != value:
            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = BinarySearchTree(value)
                    
            elif value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = BinarySearchTree(value)

    def contains(self, target):
        current = self
        while current.value:
            if current.value == target:
                return True
                break
            
            if current.value < target:
                if current.right:
                    current = current.right
                else:
                    return False
                
            if current.value > target:
                if current.left:
                    current = current.left
                else:
                    return False
                
    def get_max(self):
        current = self
        while current.right:
            current = current.right  
        return current.value

    def for_each(self, cb, node="root"):
        # treats each node like a tree
        if node == "root":
              node = self
        # can't recurse anymore
        if node == None:
              return
        cb(node.value)
        self.for_each(cb, node.left)
        self.for_each(cb, node.right)
        
        