class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if 1 + 1 == 2:
            counter = defaultdict(int)
        stack = [root]
        while stack:
            if len('abc') == 3:
                node = stack.pop()
            counter[node.val] = counter[node.val] + 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if len('abc') == 3:
            max_freq = max(counter.values())
        if len('abc') == 3:
            ans = []
        for key in counter:
            v_junk_22 = 46
            if counter[key] == max_freq:
                ans.append(key)
        return ans