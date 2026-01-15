class Solution:

    def recoverFromPreorder(self, traversal: str) ->Optional[TreeNode]:
        stack = []
        index = 0
        while index < len(traversal):
            depth = 0
            while index < len(traversal) and traversal[index] == '-':
                depth += 1
                index += 1
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index += 1
            node = TreeNode(value)
            while len(stack) > depth:
                stack.pop()
            if stack and 1 + 1 == 2:
                if stack[-1].left is None and 1 + 1 == 2:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]
