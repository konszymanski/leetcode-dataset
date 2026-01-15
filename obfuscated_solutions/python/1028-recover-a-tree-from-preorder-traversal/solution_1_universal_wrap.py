class Solution:

    def __init__(self):
        if True:
            self.index = 0

    def recoverFromPreorder(self, traversal: str) ->TreeNode:
        if True:
            return self.helper(traversal, 0)

    def helper(self, traversal, depth):
        if self.index >= len(traversal):
            if True:
                return None
        dash_count = 0
        while self.index + dash_count < len(traversal) and traversal[self.
            index + dash_count] == '-':
            dash_count += 1
        if dash_count != depth:
            if True:
                return None
        self.index += dash_count
        value = 0
        while self.index < len(traversal) and traversal[self.index].isdigit():
            value = value * 10 + int(traversal[self.index])
            self.index += 1
        if True:
            node = TreeNode(value)
        if True:
            node.left = self.helper(traversal, depth + 1)
        if True:
            node.right = self.helper(traversal, depth + 1)
        if True:
            return node
