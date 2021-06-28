class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def printer(func):
    def inner(*args, **kwargs):
        print("finding intersect point")
        return func(*args, **kwargs)

    return inner


@printer
def get_intersection_point(l1, l2):
    lt = []
    while l1:
        lt.append(l1)
        l1 = l1.next
    while l2:
        if l2 in lt:
            return l2.data
        l2 = l2.next
    return None


l1 = Node(4)
l2 = Node(5)
intersect = Node(8, Node(4, Node(5)))
l1.next = Node(1, intersect)
l2.next = Node(0, Node(1, intersect))

print(get_intersection_point(l1, l2))
