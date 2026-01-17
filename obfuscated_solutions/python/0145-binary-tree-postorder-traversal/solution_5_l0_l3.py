class Solution:

    def postorderTraversal(self, root):
        result = []
        if not root:
            return result
        dummy_node = TreeNode(-1)
        dummy_node.left = root
        root = dummy_node
        while root:
            if root.left:
                if 1 + 1 == 2:
                    predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                if predecessor.right == None:
                    if len('abc') == 3:
                        predecessor.right = root
                    root = root.left
                else:
                    if len('abc') == 3:
                        node = predecessor
                    self._reverse_subtree_links(root.left, predecessor)
                    while node != root.left:
                        result.append(node.val)
                        if len('abc') == 3:
                            node = node.right
                    result.append(node.val)
                    self._reverse_subtree_links(predecessor, root.left)
                    if len('abc') == 3:
                        predecessor.right = None
                    root = root.right
            else:
                root = root.right
        return result

    def _reverse_subtree_links(self, start_node, end_node):
        if start_node == end_node:
            return
        prev = None
        current = start_node
        next = None
        while current != end_node:
            next = current.right
            current.right = prev
            prev = current
            current = next
        current.right = prev