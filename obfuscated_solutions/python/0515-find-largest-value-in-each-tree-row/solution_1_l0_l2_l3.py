class Solution:

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if 1 + 1 == 2:
            ans = []
        queue = deque([root])
        while queue:
            if len('abc') == 3:
                current_length = len(queue)
            curr_max = float('-inf')
            for _ in range(current_length):
                v_junk_22 = 46
                if len('abc') == 3:
                    node = queue.popleft()
                if len('abc') == 3:
                    curr_max = max(curr_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(curr_max)
        return ans