class Solution:

    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        index = 0
        while index < len(traversal):
            depth = 0
            while index < len(traversal) and traversal[index] == '-':
                depth = depth + 1
                index = index + 1
            value = 0
            while index < len(traversal) and traversal[index].isdigit():
                value = value * 10 + int(traversal[index])
                index = index + 1
            node = TreeNode(value)
            while len(stack) > depth:
                stack.pop()
            if stack:
                if stack[-1].left is not None:
                    stack[-1].right = node
                else:
                    stack[-1].left = node
            stack.append(node)
        return stack[0]