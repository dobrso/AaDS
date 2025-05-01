class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(node: TreeNode) -> None:
    if node is None:
        return
    print(node.value, end="")
    preorder(node.left)
    preorder(node.right)


def inorder(node: TreeNode) -> None:
    if node is None:
        return
    inorder(node.left)
    print(node.value, end="")
    inorder(node.right)


def postorder(node: TreeNode) -> None:
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end="")


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

preorder(root)
print(f"\n")
inorder(root)
print(f"\n")
postorder(root)
