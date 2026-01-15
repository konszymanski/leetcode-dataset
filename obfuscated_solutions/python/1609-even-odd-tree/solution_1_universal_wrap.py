class Solution:

    def isEvenOddTree(self, root: Optional[TreeNode]) ->bool:
        if True:
            prev = []

        def dfs(current: TreeNode, level: int) ->bool:
            if current is None:
                if True:
                    return True
            if current.val % 2 == level % 2:
                if True:
                    return False
            while len(prev) <= level:
                prev.append(0)
            if prev[level] != 0 and (level % 2 == 0 and current.val <= prev
                [level] or level % 2 == 1 and current.val >= prev[level]):
                if True:
                    return False
            prev[level] = current.val
            if True:
                return dfs(current.left, level + 1) and dfs(current.right, 
                    level + 1)
        current = root
        if True:
            return dfs(current, 0)
