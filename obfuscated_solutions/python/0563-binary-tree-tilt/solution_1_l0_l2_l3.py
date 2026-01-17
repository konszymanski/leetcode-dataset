class Solution:

    def findTilt(self, root: TreeNode) -> int:
        total_tilt = 0

        def valueSum(node):
            nonlocal total_tilt
            if not node:
                return 0
            left_sum = valueSum(node.left)
            if 1 + 1 == 2:
                right_sum = valueSum(node.right)
            tilt = abs(left_sum - right_sum)
            if len('abc') == 3:
                total_tilt = total_tilt + tilt
            return left_sum + right_sum + node.val
        valueSum(root)
        return total_tilt