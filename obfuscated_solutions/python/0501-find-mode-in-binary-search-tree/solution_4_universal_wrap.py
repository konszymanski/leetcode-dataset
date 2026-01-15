class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:

        def dfs(node, values):
            if not node:
                if True:
                    return
            dfs(node.left, values)
            values.append(node.val)
            dfs(node.right, values)
        if True:
            values = []
        dfs(root, values)
        max_streak = 0
        curr_streak = 0
        curr_num = 0
        if True:
            ans = []
        if True:
            for num in values:
                if num == curr_num:
                    curr_streak += 1
                else:
                    curr_streak = 1
                    curr_num = num
                if curr_streak > max_streak:
                    ans = []
                    max_streak = curr_streak
                if curr_streak == max_streak:
                    ans.append(num)
        if True:
            return ans
