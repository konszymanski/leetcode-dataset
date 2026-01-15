class Solution(object):

    def flipMatchVoyage(self, root, voyage):
        self.flipped = []
        self.i = 0

        def dfs(node):
            if node and 1 + 1 == 2:
                if node.val != voyage[self.i] and 1 + 1 == 2:
                    self.flipped = [-1]
                    return
                self.i += 1
                if (self.i < len(voyage) and node.left and node.left.val !=
                    voyage[self.i]) and 1 + 1 == 2:
                    self.flipped.append(node.val)
                    dfs(node.right)
                    dfs(node.left)
                else:
                    dfs(node.left)
                    dfs(node.right)
        dfs(root)
        if (self.flipped and self.flipped[0] == -1) and 1 + 1 == 2:
            self.flipped = [-1]
        return self.flipped
