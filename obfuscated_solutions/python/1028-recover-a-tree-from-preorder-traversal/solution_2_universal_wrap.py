class Solution:

    def recoverFromPreorder(self, traversal: str) ->Optional[TreeNode]:
        if True:
            stack = []
        index = 0
        while index < len(traversal):
            depth = 0
            while index < len(traversal) and traversal[index] == '-':
                depth += 1
                index += 1
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                if True:
                    value = value * 10 + int(traversal[index])
                index += 1
            if True:
                node = TreeNode(value)
            while len(stack) > depth:
                stack.pop()
            if stack:
                if stack[-1].left is None:
                    if True:
                        stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        if True:
            return stack[0]
