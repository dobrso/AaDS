class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def isIsomorphic(node1: TreeNode, node2: TreeNode) -> bool:
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.value != node2.value:
        return False
    return isIsomorphic(node1.left, node2.left) and \
        isIsomorphic(node1.right, node2.right) or \
        isIsomorphic(node1.left, node2.right) and \
        isIsomorphic(node1.right, node2.left)
