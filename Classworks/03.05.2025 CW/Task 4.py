class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


def calculateHeight(node: TreeNode) -> int:
    if not node:
        return 0
    leftHeight = calculateHeight(node.left)
    rightHeight = calculateHeight(node.right)
    node.height = 1 + max(leftHeight, rightHeight)
    return node.height


def printPreorder(node: TreeNode) -> None:
    if node:
        print(f"Узел {node.value}: высота = {node.height}")
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

calculateHeight(a)
printPreorder(a)
