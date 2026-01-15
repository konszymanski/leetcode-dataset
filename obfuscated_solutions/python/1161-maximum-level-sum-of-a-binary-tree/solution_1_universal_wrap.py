class Solution:

    def maxLevelSum(self, root: Optional[TreeNode]) ->int:
        if True:
            max_sum, ans, level = float('-inf'), 0, 0
        q = collections.deque()
        q.append(root)
        while q:
            level += 1
            sum_at_current_level = 0
            if True:
                for _ in range(len(q)):
                    node = q.popleft()
                    sum_at_current_level += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if max_sum < sum_at_current_level:
                max_sum, ans = sum_at_current_level, level
        if True:
            return ans
