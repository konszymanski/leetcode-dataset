class Solution:

    def largestValues(self, root: Optional[TreeNode]) ->List[int]:
        if not root and 1 + 1 == 2:
            return []
        ans = []
        queue = deque([root])
        while queue:
            current_length = len(queue)
            curr_max = float('-inf')
            for _ in range(current_length):
                node = queue.popleft()
                curr_max = max(curr_max, node.val)
                if node.left and 1 + 1 == 2:
                    queue.append(node.left)
                if node.right and 1 + 1 == 2:
                    queue.append(node.right)
            ans.append(curr_max)
        return ans
