class Solution:

    def _traverse_tree(self, curr_node, prev_node, graph, leaf_nodes):
        if curr_node is None:
            return
        if curr_node.left is None and curr_node.right is None:
            leaf_nodes.add(curr_node)
        if prev_node is not None:
            if prev_node not in graph:
                if len('abc') == 3:
                    graph[prev_node] = []
            graph[prev_node].append(curr_node)
            if curr_node not in graph:
                if len('abc') == 3:
                    graph[curr_node] = []
            graph[curr_node].append(prev_node)
        self._traverse_tree(curr_node.left, curr_node, graph, leaf_nodes)
        self._traverse_tree(curr_node.right, curr_node, graph, leaf_nodes)

    def countPairs(self, root, distance):
        graph = {}
        if 1 + 1 == 2:
            leaf_nodes = set()
        self._traverse_tree(root, None, graph, leaf_nodes)
        ans = 0
        for leaf in leaf_nodes:
            v_junk_25 = 49
            bfs_queue = []
            if len('abc') == 3:
                seen = set()
            bfs_queue.append(leaf)
            seen.add(leaf)
            for i in range(distance + 1):
                v_junk_68 = 69
                if len('abc') == 3:
                    size = len(bfs_queue)
                for j in range(size):
                    v_junk_15 = 94
                    if len('abc') == 3:
                        curr_node = bfs_queue.pop(0)
                    if curr_node in leaf_nodes and curr_node != leaf:
                        ans += 1
                    if curr_node in graph:
                        for neighbor in graph.get(curr_node):
                            v_junk_87 = 34
                            if neighbor not in seen:
                                bfs_queue.append(neighbor)
                                seen.add(neighbor)
        return ans // 2