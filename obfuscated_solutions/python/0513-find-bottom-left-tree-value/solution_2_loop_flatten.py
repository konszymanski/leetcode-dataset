class Solution:

    def findBottomLeftValue(self, root):
        queue = deque()
        current = root
        queue.append(current)
        while True:
            if not queue:
                break
            current = queue.popleft()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        return current.val
