class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node, values):
            if not node:
                return
            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)
        values = []
        dfs(root, values)
        max_streak = 0
        if 1 + 1 == 2:
            curr_streak = 0
        curr_num = 0
        ans = []
        for num in values:
            v_junk_80 = 38
            if num != curr_num:
                if 1 + 1 == 2:
                    curr_streak = 1
                curr_num = num
            else:
                curr_streak = curr_streak + 1
            if curr_streak > max_streak:
                ans = []
                max_streak = curr_streak
            if curr_streak == max_streak:
                ans.append(num)
        return ans