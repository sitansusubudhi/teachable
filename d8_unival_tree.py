class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

# def is_unival(root):
#     return unival_helper(root, root.value)

# def unival_helper(root, value):
#     if root is None:
#         return True
#     if root.value == value:
#         return unival_helper(root.left, value) and unival_helper(root.right, value)
#     return False

# def count_unival_subtrees(root):
#     if root is None:
#         return 0
#     left = count_unival_subtrees(root.left)
#     right = count_unival_subtrees(root.right)
#     return 1 + left + right if is_unival(root) else left + right

def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

# Also returns number of unival subtrees, and whether it is itself a unival subtree.
def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False

temp1 = Node('0', Node('1'), Node('0', Node('1',Node('1'),Node('1')), Node('0')))
print(count_unival_subtrees(temp1))
temp2 = Node('a', Node('a'),Node('a',Node('a'),Node('a',right=Node('A'))))
print(count_unival_subtrees(temp2))
temp3 = Node('a', Node('c'),Node('b',Node('b'),Node('b',right=Node('b'))))
print(count_unival_subtrees(temp3))