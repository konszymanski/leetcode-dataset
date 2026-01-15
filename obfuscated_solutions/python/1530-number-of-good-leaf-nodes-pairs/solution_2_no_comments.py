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

        current = [0] * 12

        
        
        for i in range(10):
            current[i + 1] += left[i] + right[i]

        
        current[11] = left[11] + right[11]

        
        for d1 in range(distance + 1):
            for d2 in range(distance + 1):
                if 2 + d1 + d2 <= distance:
                    
                    
                    current[11] += left[d1] * right[d2]

        return current

    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self._post_order(root, distance)[11]