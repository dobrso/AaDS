class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.descendants = 0


def countDescendants(node: TreeNode) -> int:
    if not node:
        return 0
    leftDescendants = countDescendants(node.left)
    rightDescendants = countDescendants(node.right)

    node.descendants = leftDescendants + rightDescendants
    return node.descendants + 1


def printPreorder(node: TreeNode) -> None:
    if node:
        print(f"Узел {node.value}: потомков = {node.descendants}")
        printPreorder(node.left)
        printPreorder(node.right)


a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

a.left = b
a.right = c
b.left = d
b.right = e

countDescendants(a)
printPreorder(a)
