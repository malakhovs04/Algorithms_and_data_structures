class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.count = 1
 
class AVL:
    def __init__(self):
        self.root = None
 
    def insert(self, val):
        self.root = self._insert(self.root, val)
 
    def _insert(self, node, val):
        if not node:
            return Node(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            node.count += 1
            return node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)
 
    def _get_height(self, node):
        return node.height if node else 0
 
    def _balance(self, node):
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node
 
    def _get_balance(self, node):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0
 
    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x
 
    def _rotate_left(self, y):
        x = y.right
        T2 = x.left
        x.left = y
        y.right = T2
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        return x
 
    def get_min(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.val
 
    def get_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.val
 
    def extract_min(self):
        if not self.root:
            return None
        min_val = self.get_min()
        self.root = self._delete_min(self.root)
        return min_val
 
    def extract_max(self):
        if not self.root:
            return None
        max_val = self.get_max()
        self.root = self._delete_max(self.root)
        return max_val
 
    def _delete_min(self, node):
        if not node.left:
            if node.count > 1:
                node.count -= 1
                return node
            else:
                return node.right
        node.left = self._delete_min(node.left)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)
 
    def _delete_max(self, node):
        if not node.right:
            if node.count > 1:
                node.count -= 1
                return node
            else:
                return node.left
        node.right = self._delete_max(node.right)
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return self._balance(node)
 
 
file = open('minmax.in', 'r')
file2 = open('minmax.out', 'w')
vals = file.read().splitlines()
n = int(vals[0])
avl = AVL()
output = []
for command in vals:
    if command[0] == 'I':
        num = int(command[7:-1])
        avl.insert(num)
    elif command == "GetMin":
        min_val = avl.extract_min()
        output.append(str(min_val))
    elif command == "GetMax":
        max_val = avl.extract_max()
        output.append(str(max_val))
 
file2.write('\n'.join(output))
file.close()
file2.close()