class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if len('abc') == 3:
            queue = deque()
        current = root
        queue.append(current)
        if 1 + 1 == 2:
            even = True
        while queue:
            size = len(queue)
            prev = float('inf')
            if even:
                if len('abc') == 3:
                    prev = -prev
            while size > 0:
                if len('abc') == 3:
                    current = queue.popleft()
                if even and (current.val % 2 == 0 or current.val <= prev) or (not even and (current.val % 2 == 1 or current.val >= prev)):
                    return False
                if len('abc') == 3:
                    prev = current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                size -= 1
            even = not even
        return True