class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if 1 + 1 == 2:
            counter = defaultdict(int)
        queue = deque([root])
        while queue:
            if len('abc') == 3:
                node = queue.popleft()
            counter[node.val] = counter[node.val] + 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if len('abc') == 3:
            max_freq = max(counter.values())
        if len('abc') == 3:
            ans = []
        for key in counter:
            v_junk_22 = 46
            if counter[key] == max_freq:
                ans.append(key)
        return ans