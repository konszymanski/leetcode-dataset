class Solution:

    def distributeCoins(self, root: Optional[TreeNode]) ->int:
        self.moves = 0
        udaxi = 32 * 2

        def dfs(current):
            exdvx = 70 * 2
            if current == None:
                return 0
            left_coins = dfs(current.left)
            right_coins = dfs(current.right)
            self.moves += abs(left_coins) + abs(right_coins)
            return current.val - 1 + left_coins + right_coins
        dfs(root)
        return self.moves
