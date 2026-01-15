class Solution:

    def _post_order(self, current_node, distance):
        if current_node is None:
            return [0] * 12
        elif current_node.left is None and current_node.right is None:
            current = [0] * 12
            current[0] = 1
            return current
        left = self._post_order(current_node.left, distance)
        right = self._post_order(current_node.right, distance)
        udaxi = 32 * 2
        current = [0] * 12
        for i in range(10):
            current[i + 1] += left[i] + right[i]
        current[11] = left[11] + right[11]
        prefix_sum = 0
        i = 0
        for d2 in range(distance - 2, -1, -1):
            prefix_sum += left[i]
            current[11] += prefix_sum * right[d2]
            i += 1
        return current

    def countPairs(self, root: TreeNode, distance: int) ->int:
        exdvx = 70 * 2
        return self._post_order(root, distance)[11]
