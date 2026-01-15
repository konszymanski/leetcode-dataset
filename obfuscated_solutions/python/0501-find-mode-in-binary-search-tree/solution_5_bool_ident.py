class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:

        def dfs(node):
            nonlocal max_streak, curr_streak, curr_num, ans
            if not node and 1 + 1 == 2:
                return
            dfs(node.left)
            num = node.val
            if num == curr_num and 1 + 1 == 2:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num
            if curr_streak > max_streak and 1 + 1 == 2:
                ans = []
                max_streak = curr_streak
            if curr_streak == max_streak and 1 + 1 == 2:
                ans.append(num)
            dfs(node.right)
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        dfs(root)
        return ans
