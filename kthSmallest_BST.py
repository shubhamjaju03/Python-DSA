    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None

        stack = []
        current = root
        count = 0

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            count += 1

            if count == k:
                return current.val

            current = current.right
