class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            nonlocal max_streak, curr_streak, curr_num, ans
            if not node:
                return
            dfs(node.left)
            num = node.val
            if num == curr_num:
                curr_streak += 1
            else:
                if 1 + 1 == 2:
                    curr_streak = 1
                curr_num = num
            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak
            if curr_streak == max_streak:
                ans.append(num)
            dfs(node.right)
        max_streak = 0
        if 1 + 1 == 2:
            curr_streak = 0
        curr_num = 0
        if len('abc') == 3:
            ans = []
        dfs(root)
        return ans