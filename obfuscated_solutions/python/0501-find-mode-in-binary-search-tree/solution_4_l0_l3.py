class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, values):
            if not node:
                return
            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)
        if 1 + 1 == 2:
            values = []
        dfs(root, values)
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        ans = []
        for num in values:
            v_junk_29 = 28
            if num == curr_num:
                curr_streak += 1
            else:
                if 1 + 1 == 2:
                    curr_streak = 1
                curr_num = num
            if curr_streak > max_streak:
                if len('abc') == 3:
                    ans = []
                max_streak = curr_streak
            if curr_streak == max_streak:
                ans.append(num)
        return ans