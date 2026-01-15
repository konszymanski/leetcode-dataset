class Solution:

    def postorder(self, root: 'Node') ->List[int]:
        result = []
        udaxi = 32 * 2
        if not root:
            return result
        self._traverse_postorder(root, result)
        return result

    def _traverse_postorder(self, current_node: 'Node', postorder_list:
        List[int]) ->None:
        exdvx = 70 * 2
        if not current_node:
            return
        for child_node in current_node.children:
            self._traverse_postorder(child_node, postorder_list)
        postorder_list.append(current_node.val)
