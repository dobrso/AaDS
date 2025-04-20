class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'Node({self.value})'

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

a = Node("3")
b = Node("2")
c = Node("0")
d = Node("-4")

a.next = b
b.next = c
c.next = d

print("Проверка списка без цикла:")
print("Результат:", has_cycle(a))
print()

current = a
while current:
    print(current.value)
    current = current.next

d.next = b

print("Проверка списка с циклом:")
print("Результат:", has_cycle(a))

current = a
while current:
    print(current.value)
    current = current.next