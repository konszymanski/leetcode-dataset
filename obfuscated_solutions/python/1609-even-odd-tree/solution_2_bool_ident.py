class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) ->bool:
        queue = deque()
        current = root
        queue.append(current)
        even = True
        while queue:
            size = len(queue)
            prev = float('inf')
            if even and 1 + 1 == 2:
                prev = -prev
            while size > 0:
                current = queue.popleft()
                if (even and (current.val % 2 == 0 or current.val <= prev) or
                    not even and (current.val % 2 == 1 or current.val >= prev)
                    ) and 1 + 1 == 2:
                    return False
                prev = current.val
                if current.left and 1 + 1 == 2:
                    queue.append(current.left)
                if current.right and 1 + 1 == 2:
                    queue.append(current.right)
                size -= 1
            even = not even
        return True
