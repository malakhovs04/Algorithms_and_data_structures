class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None


    # Поиск значения в дереве
    def find(self, val):
        current = self.root
        while current is not None:
            if current.val == val:
                return current
            current = current.left if val < current.val else current.right
        return None

    # Вставка значения в дерево
    def insert(self, val):
        self.root = insert_avl(self.root, val)

    # Удаление значения из дерева
    def erase(self, key):
        self.root = erase_avl(self.root, key)

    # Проверка является ли дерево BST
    def is_valid_bst(self):
        return valid(self.root, float('-inf'), float('inf'))

    # Симметричный обход (левое поддерево -> корень -> правое поддерево)
    def inorder(self):
        result = []
        inorder_tree(self.root, result)
        return result

    # Прямой обход (корень -> левое поддерево -> правое поддерево)
    def preorder(self):
        result = []
        preorder_tree(self.root, result)
        return result

    # Обратный обход (левое поддерево -> правое поддерево -> корень)
    def postorder(self):
        result = []
        postorder_tree(self.root, result)
        return result

    # Удаление всего дерева
    def delete_tree(self):
        if self.root:
            delete_tree(self.root)
            self.root = None

def height(node):
    return node.height if node else 0

def update_height(node):
    if node:
        node.height = 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)
    return x


def rotate_left(y):
    x = y.right
    T2 = x.left

    x.left = y
    y.right = T2

    update_height(x)
    update_height(y)
    return x

def balance(node):
    if not node:
        return node
    update_height(node)
    balance_k = balance_factor(node)

    if balance_k < -1:
        if balance_factor(node.right) > 0:
            node.right = rotate_right(node.right)
        return rotate_left(node)

    if balance_k > 1:
        if balance_factor(node.left) < 0:
            node.left = rotate_left(node.left)
        return rotate_right(node)

    return node

def insert_avl(node, val):
    if not node:
        return Node(val)
    if val < node.val:
        node.left = insert_avl(node.left, val)
    else:
        node.right = insert_avl(node.right, val)
    return balance(node)


def erase_avl(node, key):
    if node is None:
        return node
    if key < node.val:
        node.left = erase_avl(node.left, key)
    elif key > node.val:
        node.right = erase_avl(node.right, key)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        temp = node.right
        while temp.left:
            temp = temp.left
        node.val = temp.val
        node.right = erase_avl(node.right, node.val)
    return balance(node)


def valid(node, left, right):
    if not node:
        return True
    if not (node.val < right and node.val > left):
        return False
    return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))

def inorder_tree(root, res):
    if root:
        inorder_tree(root.left, res)
        res.append(root.val)
        inorder_tree(root.right, res)


def preorder_tree(root, res):
    if root:
        res.append(root.val)
        preorder_tree(root.left, res)
        preorder_tree(root.right, res)


def postorder_tree(root, res):
    if root:
        postorder_tree(root.left, res)
        postorder_tree(root.right, res)
        res.append(root.val)


def delete_tree(root):
    if root.left:
        delete_tree(root.left)
        root.left = None
    if root.right:
        delete_tree(root.right)
        root.right = None
    root = None


avl = AVL()

# Вставляем значения в дерево
for val in [5, 3, 7, 2, 4, 11, 9, 10, 8]:
    avl.insert(val)

# Выводим обходы дерева
print("Inorder обход:", avl.inorder())  # [2, 3, 4, 5, 6, 7, 8]
print("Preorder обход:", avl.preorder())  # [5, 3, 2, 4, 7, 6, 8]
print("Postorder обход:", avl.postorder())  # [2, 4, 3, 6, 8, 7, 5]

# Поиск значений
print("Найдено 4:", avl.find(4) is not None)  # True
print("Найдено 10:", avl.find(10) is not None)  # False

# Удаление узла
avl.erase(3)
print("После удаления 3, Inorder:", avl.inorder())  # [2, 4, 5, 6, 7, 8]

# Проверка корректности дерева
print("Является BST:", avl.is_valid_bst())  # True

# Удаление всего дерева
avl.delete_tree()
print("После удаления дерева, Inorder:", avl.inorder())  # []
