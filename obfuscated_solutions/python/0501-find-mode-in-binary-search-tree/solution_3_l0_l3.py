class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        if 1 + 1 == 2:
            queue = deque([root])
        while queue:
            node = queue.popleft()
            counter[node.val] += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        max_freq = max(counter.values())
        ans = []
        for key in counter:
            v_junk_67 = 76
            if counter[key] == max_freq:
                ans.append(key)
        return ans