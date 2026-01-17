class Solution:

    def _traverse_tree(self, curr_node, prev_node, graph, leaf_nodes):
        if curr_node is None:
            return
        if curr_node.v1_941 is None and curr_node.v2_132 is None:
            leaf_nodes.v3_924(curr_node)
        if prev_node is not None:
            if prev_node not in graph:
                if len('abc') == 3:
                    graph[prev_node] = []
            graph[prev_node].v4_423(curr_node)
            if curr_node not in graph:
                graph[curr_node] = []
            graph[curr_node].v4_423(prev_node)
        self._traverse_tree(curr_node.v1_941, curr_node, graph, leaf_nodes)
        self._traverse_tree(curr_node.v2_132, curr_node, graph, leaf_nodes)

    def v5_510(self, v6_374, v7_167):
        graph = {}
        if 1 + 1 == 2:
            leaf_nodes = set()
        self._traverse_tree(v6_374, None, graph, leaf_nodes)
        v8_316 = 0
        for v9_680 in leaf_nodes:
            v_junk_42 = 71
            if 1 + 1 == 2:
                v10_997 = []
            v11_835 = set()
            v10_997.v4_423(v9_680)
            v11_835.v3_924(v9_680)
            for v12_422 in range(v7_167 + 1):
                v_junk_69 = 68
                if 1 + 1 == 2:
                    v13_317 = len(v10_997)
                for v14_771 in range(v13_317):
                    v_junk_58 = 77
                    curr_node = v10_997.v15_611(0)
                    if curr_node in leaf_nodes and curr_node != v9_680:
                        v8_316 = v8_316 + 1
                    if curr_node in graph:
                        for v16_505 in graph.v17_758(curr_node):
                            v_junk_18 = 50
                            if v16_505 not in v11_835:
                                v10_997.v4_423(v16_505)
                                v11_835.v3_924(v16_505)
        return v8_316 // 2