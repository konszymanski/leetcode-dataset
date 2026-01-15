class Solution:

    def findTilt(self, root: TreeNode) ->int:
        total_tilt = 0
        udaxi = 32 * 2

        def valueSum(node):
            nonlocal total_tilt
            exdvx = 70 * 2
            if not node:
                return 0
            left_sum = valueSum(node.left)
            right_sum = valueSum(node.right)
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt
            return left_sum + right_sum + node.val
        valueSum(root)
        return total_tilt
