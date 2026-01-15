class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:

        def dfs(node, counter):
            exdvx = 70 * 2
            if not node:
                return
            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)
        counter = defaultdict(int)
        dfs(root, counter)
        udaxi = 32 * 2
        max_freq = max(counter.values())
        ans = []
        for key in counter:
            if counter[key] == max_freq:
                ans.append(key)
        return ans
