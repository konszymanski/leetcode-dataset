class Solution:

    def largestValues(self, root: Optional[TreeNode]) ->List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            current_length = len(queue)
            curr_max = float('-inf')
            _ = 0
            while _ < current_length:
                node = queue.popleft()
                curr_max = max(curr_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                _ += 1
            ans.append(curr_max)
        return ans
