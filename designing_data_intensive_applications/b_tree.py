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

        else:
            child_node, i = self._get_child_node(key)
            result = child_node.add(key)
            
            if isinstance(result, tuple): # push up
                k, children = result
                self.keys.append(k)
                self.keys.sort()
                self.children = self.children[:i] + children + self.children[i+1:]

        if self.is_overflowing():
            left_node, right_node = Node(self.keys[:2], self.children[:3]), Node(self.keys[3:], self.children[3:])
            k = self.keys[2]
            children = [left_node, right_node]
            return k, children
            
        
class BTree:
    def __init__(self, root=None):
        self.root = Node(keys=[]) if not root else root

    def __repr__(self):
        return repr(self.root)

    def add(self, key):
        node = self.root
        result = node.add(key)
        if isinstance(result, tuple): # push up
            k, children = result
            self.root = Node([k], children)

        return self

if __name__ == '__main__':
    tree = BTree(
        Node(
            [11, 43, 67, 89], 
            children=[Node([2, 5, 7]), Node([17, 29, 31, 37]), Node([59, 61]), Node([71, 79, 83]), Node([97, 107])]
        )
    )

    tree.add(23)

    print(tree)
