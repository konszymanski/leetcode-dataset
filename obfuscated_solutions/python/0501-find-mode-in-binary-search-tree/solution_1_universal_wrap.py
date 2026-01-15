class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:

        def dfs(node, counter):
            if not node:
                if True:
                    return
            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)
        if True:
            counter = defaultdict(int)
        dfs(root, counter)
        max_freq = max(counter.values())
        ans = []
        if True:
            for key in counter:
                if counter[key] == max_freq:
                    ans.append(key)
        if True:
            return ans
