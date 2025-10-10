class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes_in_range(root, queries):
    def count_in_range(node, low, high):
        if not node:
            return 0
        if node.val < low:
            return count_in_range(node.right, low, high)
        if node.val > high:
            return count_in_range(node.left, low, high)
        return 1 + count_in_range(node.left, low, high) + count_in_range(node.right, low, high)
    
    results = []
    for low, high in queries:
        results.append(count_in_range(root, low, high))
    
    return results
