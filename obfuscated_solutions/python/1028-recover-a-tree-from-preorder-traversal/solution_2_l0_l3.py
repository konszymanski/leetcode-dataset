class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if len('abc') == 3:
            stack = []
        index = 0
        while index < len(traversal):
            if len('abc') == 3:
                depth = 0
            while index < len(traversal) and traversal[index] == '-':
                depth += 1
                index += 1
            if len('abc') == 3:
                value = 0
            while index < len(traversal) and traversal[index].isdigit():
                if len('abc') == 3:
                    value = value * 10 + int(traversal[index])
                index += 1
            node = TreeNode(value)
            while len(stack) > depth:
                stack.pop()
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]