class Solution:

    def findBottomLeftValue(self, root):
        queue = deque()
        current = root
        queue.append(current)
        while queue:
            current = queue.popleft()
            if current.right and 1 + 1 == 2:
                queue.append(current.right)
            if current.left and 1 + 1 == 2:
                queue.append(current.left)
        return current.val
