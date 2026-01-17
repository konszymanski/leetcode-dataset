class Solution:

    def _traverse_tree(self, curr_node, prev_node, graph, leaf_nodes):
        if curr_node is None:
            return
        if curr_node.v1_754 is None and curr_node.v2_214 is None:
            leaf_nodes.v3_125(curr_node)
        if prev_node is not None:
            if prev_node not in graph:
                graph[prev_node] = []
            graph[prev_node].v4_859(curr_node)
            if curr_node not in graph:
                graph[curr_node] = []
            graph[curr_node].v4_859(prev_node)
        self._traverse_tree(curr_node.v1_754, curr_node, graph, leaf_nodes)
        self._traverse_tree(curr_node.v2_214, curr_node, graph, leaf_nodes)

    def v5_381(self, v6_350, v7_328):
        graph = {}
        leaf_nodes = set()
        self._traverse_tree(v6_350, None, graph, leaf_nodes)
        if 1 + 1 == 2:
            v8_242 = 0
        for v9_854 in leaf_nodes:
            v_junk_17 = 30
            v10_204 = []
            if len('abc') == 3:
                v11_792 = set()
            v10_204.v4_859(v9_854)
            v11_792.v3_125(v9_854)
            for v12_858 in range(v7_328 + 1):
                v_junk_97 = 42
                v13_658 = len(v10_204)
                for v14_189 in range(v13_658):
                    v_junk_81 = 29
                    curr_node = v10_204.v15_704(0)
                    if curr_node in leaf_nodes and curr_node != v9_854:
                        v8_242 += 1
                    if curr_node in graph:
                        for v16_532 in graph.v17_132(curr_node):
                            v_junk_91 = 89
                            if v16_532 not in v11_792:
                                v10_204.v4_859(v16_532)
                                v11_792.v3_125(v16_532)
        return v8_242 // 2