class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.key = 0

    def __str__(self):
        return str(self.key)


# 8--->4, 2 (4)---> 2, 2

def new_node(key):
    n = Node()
    n.key = key
    return n


def create_factor_tree(node):
    root = node.key
    if root % 2 != 0 or root // 2 == 1:
        return node
    node.left = create_factor_tree(new_node(2))
    node.right = create_factor_tree(new_node(root // 2))
    return node


def traverse_tree(N):
    n = create_factor_tree(new_node(N))
    l = [n]
    count = 0
    print(" ", end="")
    while l:
        n1 = l.pop(0)
        if count % 2 == 0:
            print(" ", end="")
            print(n1)
        else:
            print(" " * (count or 1), end="")
            print(n1, end="")
        if count % 2 == 0 and n1.right:
            print(" " * ((count or 1) + 1), end="")
            print("/\\")
        if n1.left:
            l.append(n1.left)
        if n1.right:
            l.append(n1.right)
        count += 1


def solve(N):
    n = create_factor_tree(new_node(N))
    count = 0
    while n:
        if n.right:
            count += 1
        n = n.right
    return count


N = int(input())

# out_ = solve(N)
# print(out_)
traverse_tree(N)
