class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if root is None:
        return '#'
    # print('{} {} {}'.format(root.val, serialize(root.left), serialize(root.right)))
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(str(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()

node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left'
assert deserialize(serialize(node)).left.left.val == 'left.left'
print("success")