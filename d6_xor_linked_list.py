import ctypes


# This is hacky. It's a data structure for C, not python.
class Node(object):
    def __init__(self, val):
        self.val = val
        self.both = 0


class XorLinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = [] # This is to prevent garbage collection

    def add(self, node):
        if self.head is None:
            self.head = self.tail = node
            # print('self.tail.both initial',self.tail.both)
        else:
            # print('self.tail.both 2nd time before changing',self.tail.both)
            self.tail.both = id(node) ^ self.tail.both
            # print('self.tail.both 2nd time after changing',self.tail.both)
            node.both = id(self.tail)
            self.tail = node
            # print('self.tail.both final after changing',self.tail.both)

        # Without this line, Python thinks there is no way to reach nodes between
        # head and tail.
        self.__nodes.append(node)


    def get(self, index):
        prev_id = 0
        node = self.head
        for _ in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = id(node)
                node = _get_obj(next_id)
            else:
                raise IndexError('Linked list index out of range')
        # print('id',id(node))
        return node


def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value

xor_list = XorLinkedList()
xor_list.add(Node(5))
xor_list.add(Node(6))
# xor_list.add(Node(7))
# xor_list.add(Node(8))
# xor_list.add(Node(1))
# xor_list.add(Node(2))
print(xor_list.get(0).both)
print(xor_list.get(1).both)
