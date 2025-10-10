class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_predecessor_successor(root, key):
    predecessor = None
    successor = None
    current = root

    while current:
        if key < current.val:
            successor = current.val
            current = current.left
        elif key > current.val:
            predecessor = current.val
            current = current.right
        else:
            temp = current.left
            while temp:
                predecessor = temp.val
                temp = temp.right
            temp = current.right
            while temp:
                successor = temp.val
                temp = temp.left
            break
    return (predecessor, successor)

