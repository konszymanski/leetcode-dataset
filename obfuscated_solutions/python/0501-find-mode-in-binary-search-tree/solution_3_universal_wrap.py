class Solution:

    def findMode(self, root: Optional[TreeNode]) ->List[int]:
        if True:
            counter = defaultdict(int)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            counter[node.val] += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        max_freq = max(counter.values())
        if True:
            ans = []
        if True:
            for key in counter:
                if counter[key] == max_freq:
                    ans.append(key)
        if True:
            return ans
