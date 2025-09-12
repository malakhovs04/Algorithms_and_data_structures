class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
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
        if self.root is None:
            self.root = Node(val)
        else:
            insert_bst(self.root, val)


    # Удаление значения из дерева
    def erase(self, key):
        return erase_bst(self.root, key)


    # Проверка является ли дерево BST
    def is_valid_bst(self):
        return valid(self.root, float('-inf'), float('inf'))


    # Симметричный обход (левое поддерево -> корень -> правое поддерево)
    def inorder(self):
        result = []
        inorder_bst(self.root, result)
        return result


    # Прямой обход (корень -> левое поддерево -> правое поддерево)
    def preorder(self):
        result = []
        preorder_bst(self.root, result)
        return result


    # Обратный обход (левое поддерево -> правое поддерево -> корень)
    def postorder(self):
        result = []
        postorder_bst(self.root, result)
        return result
    

    # Удаление всего дерева
    def delete_tree(self):
        if self.root:
            delete_bst(self.root)
            self.root = None


def insert_bst(node, val):
    if val < node.val:
        if node.left is None:
            node.left = Node(val)
        else:
            insert_bst(node.left, val)
    else:
        if node.right is None:
            node.right = Node(val)
        else:
            insert_bst(node.right, val)


def erase_bst(node, key):
    if node is None:
        return node
    if key < node.val:
        node.left = erase_bst(node.left, key)
    elif key > node.val:
        node.right = erase_bst(node.right, key)
    else:
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        temp = node.right
        while temp.left:
            temp = temp.left
        node.val = temp.val
        node.right = erase_bst(node.right, node.val)
    return node


def valid(node, left, right):
    if not node:
        return True
    if not (node.val < right and node.val > left):
        return False
    return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))


def inorder_bst(root, res):
    if root:
        inorder_bst(root.left, res)
        res.append(root.val)
        inorder_bst(root.right, res)


def preorder_bst(root, res):
    if root:
        res.append(root.val)
        preorder_bst(root.left, res)
        preorder_bst(root.right, res)


def postorder_bst(root, res):
    if root:
        postorder_bst(root.left, res)
        postorder_bst(root.right, res)
        res.append(root.val)


def delete_bst(root):
    if root.left:
        delete_bst(root.left)
        root.left = None
    if root.right:
        delete_bst(root.right)
        root.right = None
    root = None


bst = BST()

# Вставляем значения в дерево
for val in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(val)

# Выводим обходы дерева
print("Inorder обход:", bst.inorder())    # [2, 3, 4, 5, 6, 7, 8]
print("Preorder обход:", bst.preorder()) # [5, 3, 2, 4, 7, 6, 8]
print("Postorder обход:", bst.postorder()) # [2, 4, 3, 6, 8, 7, 5]

# Поиск значений
print("Найдено 4:", bst.find(4) is not None)  # True
print("Найдено 10:", bst.find(10) is not None) # False

# Удаление узла
bst.erase(3)
print("После удаления 3, Inorder:", bst.inorder()) # [2, 4, 5, 6, 7, 8]

# Проверка корректности дерева
print("Является BST:", bst.is_valid_bst()) # True

# Удаление всего дерева
bst.delete_tree()
print("После удаления дерева, Inorder:", bst.inorder()) # []
