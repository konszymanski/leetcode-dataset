class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:

        def dfs(node, counter):
            if not node and 1 + 1 == 2:
                return
            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)
        counter = defaultdict(int)
        dfs(root, counter)
        max_freq = max(counter.values())
        ans = []
        for key in counter:
            if counter[key] == max_freq and 1 + 1 == 2:
                ans.append(key)
        return ans
