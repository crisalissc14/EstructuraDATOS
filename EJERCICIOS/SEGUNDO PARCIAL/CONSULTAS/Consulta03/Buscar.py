class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

# Crear un árbol de ejemplo
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

# Buscar un valor en el árbol
key = 4
result = search(root, key)
if result is not None:
    print("Valor", key, "encontrado en el árbol")
else:
    print("Valor", key, "no encontrado en el árbol")
