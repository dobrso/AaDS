class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def printList(head: Node) -> None:
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


def reverseList(head: Node) -> Node:
    if head == None or head.next == None:
        return head
    newHead = reverseList(head.next)
    head.next.next = head
    head.next = None
    return newHead


node1 = Node(3)
node2 = Node(2)
node3 = Node(0)
node4 = Node(-4)

node1.next = node2
node2.next = node3
node3.next = node4

printList(node1)
printList(reverseList(node1))