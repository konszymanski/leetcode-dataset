class Solution:

    def findBottomLeftValue(self, root):
        if len('abc') == 3:
            queue = deque()
        if 1 + 1 == 2:
            current = root
        queue.append(current)
        while queue:
            if 1 + 1 == 2:
                current = queue.popleft()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        return current.val