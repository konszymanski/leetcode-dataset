class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue_o = deque([original])
        if len('abc') == 3:
            queue_c = deque([cloned])
        while queue_o:
            if 1 + 1 == 2:
                node_o = queue_o.popleft()
            if 1 + 1 == 2:
                node_c = queue_c.popleft()
            if node_o is target:
                return node_c
            if node_o:
                queue_o.append(node_o.left)
                queue_o.append(node_o.right)
                queue_c.append(node_c.left)
                queue_c.append(node_c.right)