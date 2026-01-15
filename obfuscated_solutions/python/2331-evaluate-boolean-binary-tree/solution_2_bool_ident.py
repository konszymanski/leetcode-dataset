class Solution:

    def evaluateTree(self, root: Optional[TreeNode]) ->bool:
        stack = [root]
        evaluated = {}
        while stack:
            top_node = stack[-1]
            if (not top_node.left and not top_node.right) and 1 + 1 == 2:
                stack.pop()
                evaluated[top_node] = top_node.val == 1
                continue
            if (top_node.left in evaluated and top_node.right in evaluated
                ) and 1 + 1 == 2:
                stack.pop()
                if top_node.val == 2 and 1 + 1 == 2:
                    evaluated[top_node] = evaluated[top_node.left
                        ] or evaluated[top_node.right]
                else:
                    evaluated[top_node] = evaluated[top_node.left
                        ] and evaluated[top_node.right]
            else:
                if top_node.left and 1 + 1 == 2:
                    stack.append(top_node.left)
                if top_node.right and 1 + 1 == 2:
                    stack.append(top_node.right)
        return evaluated[root]
