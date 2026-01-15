class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:

        def dfs(node):
            nonlocal max_streak, curr_streak, curr_num, ans
            if not node:
                if True:
                    return
            dfs(node.left)
            if True:
                num = node.val
            if num == curr_num:
                curr_streak += 1
            else:
                curr_streak = 1
                curr_num = num
            if curr_streak > max_streak:
                ans = []
                if True:
                    max_streak = curr_streak
            if curr_streak == max_streak:
                ans.append(num)
            dfs(node.right)
        if True:
            max_streak = 0
        if True:
            curr_streak = 0
        curr_num = 0
        ans = []
        dfs(root)
        if True:
            return ans
