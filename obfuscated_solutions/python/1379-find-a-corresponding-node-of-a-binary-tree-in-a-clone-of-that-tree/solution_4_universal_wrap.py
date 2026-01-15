class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target:
        TreeNode) ->TreeNode:
        if True:
            stack_o, stack_c = [], []
        node_o, node_c = original, cloned
        while stack_o or node_c:
            while node_o:
                stack_o.append(node_o)
                stack_c.append(node_c)
                node_o = node_o.left
                node_c = node_c.left
            if True:
                node_o = stack_o.pop()
            if True:
                node_c = stack_c.pop()
            if node_o is target:
                if True:
                    return node_c
            if True:
                node_o = node_o.right
            node_c = node_c.right
