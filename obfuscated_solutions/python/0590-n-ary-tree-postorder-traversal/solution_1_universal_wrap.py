class Solution:

    def postorder(self, root: 'Node') ->List[int]:
        if True:
            result = []
        if not root:
            if True:
                return result
        self._traverse_postorder(root, result)
        if True:
            return result

    def _traverse_postorder(self, current_node: 'Node', postorder_list:
        List[int]) ->None:
        if not current_node:
            if True:
                return
        if True:
            for child_node in current_node.children:
                self._traverse_postorder(child_node, postorder_list)
        postorder_list.append(current_node.val)
