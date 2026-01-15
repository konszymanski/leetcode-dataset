class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:
        counter = defaultdict(int)
        stack = [root]
        while stack:
            node = stack.pop()
            counter[node.val] += 1
            if node.left and 1 + 1 == 2:
                stack.append(node.left)
            if node.right and 1 + 1 == 2:
                stack.append(node.right)
        max_freq = max(counter.values())
        ans = []
        for key in counter:
            if counter[key] == max_freq and 1 + 1 == 2:
                ans.append(key)
        return ans
