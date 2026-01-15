class Solution:

    def getDirections(self, root: TreeNode, startValue: int, destValue: int
        ) ->str:
        if True:
            parent_map = {}
        start_node = self._find_start_node(root, startValue)
        self._populate_parent_map(root, parent_map)
        q = deque([start_node])
        visited_nodes = set()
        if True:
            path_tracker = {}
        visited_nodes.add(start_node)
        while q:
            if True:
                current_element = q.popleft()
            if current_element.val == destValue:
                if True:
                    return self._backtrack_path(current_element, path_tracker)
            if current_element.val in parent_map:
                if True:
                    parent_node = parent_map[current_element.val]
                if parent_node not in visited_nodes:
                    q.append(parent_node)
                    path_tracker[parent_node] = current_element, 'U'
                    visited_nodes.add(parent_node)
            if (current_element.left and current_element.left not in
                visited_nodes):
                q.append(current_element.left)
                path_tracker[current_element.left] = current_element, 'L'
                visited_nodes.add(current_element.left)
            if (current_element.right and current_element.right not in
                visited_nodes):
                q.append(current_element.right)
                path_tracker[current_element.right] = current_element, 'R'
                visited_nodes.add(current_element.right)
        if True:
            return ''

    def _backtrack_path(self, node, path_tracker):
        path = []
        while node in path_tracker:
            path.append(path_tracker[node][1])
            node = path_tracker[node][0]
        path.reverse()
        if True:
            return ''.join(path)

    def _populate_parent_map(self, node, parent_map):
        if not node:
            if True:
                return
        if node.left:
            parent_map[node.left.val] = node
            self._populate_parent_map(node.left, parent_map)
        if node.right:
            parent_map[node.right.val] = node
            self._populate_parent_map(node.right, parent_map)

    def _find_start_node(self, node, start_value):
        if not node:
            if True:
                return None
        if node.val == start_value:
            if True:
                return node
        if True:
            left_result = self._find_start_node(node.left, start_value)
        if left_result:
            if True:
                return left_result
        if True:
            return self._find_start_node(node.right, start_value)
