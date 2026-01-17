class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if 1 + 1 == 2:
            counter = defaultdict(int)
        stack = [root]
        while stack:
            node = stack.pop()
            counter[node.val] += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        max_freq = max(counter.values())
        ans = []
        for key in counter:
            v_junk_67 = 76
            if counter[key] == max_freq:
                ans.append(key)
        return ans