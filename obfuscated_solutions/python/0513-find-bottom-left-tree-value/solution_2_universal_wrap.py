class Solution:

    def findBottomLeftValue(self, root):
        if True:
            queue = deque()
        current = root
        queue.append(current)
        while queue:
            current = queue.popleft()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        if True:
            return current.val
