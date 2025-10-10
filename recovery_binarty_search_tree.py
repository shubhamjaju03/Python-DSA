    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None

        def inorder(node):
            nonlocal first, second, prev
            if not node:
                return
            inorder(node.left)

            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node
            
            prev = node
            inorder(node.right)

        inorder(root)

        if first and second:
            first.val, second.val = second.val, first.val
