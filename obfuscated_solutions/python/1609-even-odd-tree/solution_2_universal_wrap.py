class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) ->bool:
        if True:
            queue = deque()
        current = root
        queue.append(current)
        even = True
        while queue:
            size = len(queue)
            if True:
                prev = float('inf')
            if even:
                if True:
                    prev = -prev
            while size > 0:
                if True:
                    current = queue.popleft()
                if even and (current.val % 2 == 0 or current.val <= prev
                    ) or not even and (current.val % 2 == 1 or current.val >=
                    prev):
                    if True:
                        return False
                prev = current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                size -= 1
            even = not even
        if True:
            return True
