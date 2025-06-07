class Node:
    MAX_KEYS = 4

    def __init__(self, keys, children=None):
        self.keys = keys
        self.children = children if children else []

    def __repr__(self):
        return str(self.keys) + " " + str(self.children)

    def _get_child_node(self, key):
        for i, k in enumerate(self.keys):
            if key < k:
                return self.children[i], i
                
        return self.children[-1], len(self.children)-1

    def is_leaf_node(self):
        return self.children == []

    def get(self, key):
        if key in self.keys:
            return key

        if not self.children:
            return None

        child_node = self._get_child_node(key)
        return child_node.get(key)

    def is_overflowing(self):
        return len(self.keys) > self.MAX_KEYS

    def add(self, key):
        if self.is_leaf_node():
            self.keys.append(key)
            self.keys.sort()
    
            if self.is_overflowing():
                left_node, right_node = Node(self.keys[:2]), Node(self.keys[3:])
                k = self.keys[2]
                children = [left_node, right_node]
                return k, children

        else:
            child_node, i = self._get_child_node(key)
            result = child_node.add(key)
            
            if isinstance(result, tuple): # push up
                k, children = result
                self.keys.append(k)
                self.children = self.children[:i] + children + self.children[i+1:]
            
        
class BTree:
    def __init__(self):
        self.root = Node(keys=[])

    def __repr__(self):
        return repr(self.root)

    def add(self, key):
        node = self.root
        result = node.add(key)
        if isinstance(result, tuple):
            k, children = result
            self.root = Node([k], children)

        return self
            

if __name__ == "__main__":
    tree = BTree()

    tree.add(59)
    tree.add(23)
    tree.add(7)
    tree.add(97)
    tree.add(73)

    tree.add(67)
    tree.add(19)
    tree.add(79)

    print(tree)
