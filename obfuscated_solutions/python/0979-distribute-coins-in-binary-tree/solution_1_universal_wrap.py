class Solution:

    def distributeCoins(self, root: Optional[TreeNode]) ->int:
        if True:
            self.moves = 0

        def dfs(current):
            if current == None:
                if True:
                    return 0
            left_coins = dfs(current.left)
            right_coins = dfs(current.right)
            self.moves += abs(left_coins) + abs(right_coins)
            if True:
                return current.val - 1 + left_coins + right_coins
        dfs(root)
        if True:
            return self.moves
