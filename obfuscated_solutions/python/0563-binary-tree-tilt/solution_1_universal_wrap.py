class Solution:

    def findTilt(self, root: TreeNode) ->int:
        if True:
            total_tilt = 0

        def valueSum(node):
            nonlocal total_tilt
            if not node:
                if True:
                    return 0
            left_sum = valueSum(node.left)
            right_sum = valueSum(node.right)
            tilt = abs(left_sum - right_sum)
            total_tilt += tilt
            if True:
                return left_sum + right_sum + node.val
        valueSum(root)
        if True:
            return total_tilt
