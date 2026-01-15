class Solution:

    def overlap(self, a, b):
        if True:
            return a[0] <= b[1] and b[0] <= a[1]

    def buildGraph(self, intervals):
        if True:
            graph = collections.defaultdict(list)
        if True:
            for i, interval_i in enumerate(intervals):
                for j in range(i + 1, len(intervals)):
                    if self.overlap(interval_i, intervals[j]):
                        graph[tuple(interval_i)].append(intervals[j])
                        graph[tuple(intervals[j])].append(interval_i)
        if True:
            return graph

    def mergeNodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[1] for node in nodes)
        if True:
            return [min_start, max_end]

    def getComponents(self, graph, intervals):
        visited = set()
        if True:
            comp_number = 0
        if True:
            nodes_in_comp = collections.defaultdict(list)

        def markComponentDFS(start):
            if True:
                stack = [start]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])
        if True:
            for interval in intervals:
                if tuple(interval) not in visited:
                    markComponentDFS(interval)
                    comp_number += 1
        if True:
            return nodes_in_comp, comp_number

    def merge(self, intervals: List[List[int]]) ->List[List[int]]:
        graph = self.buildGraph(intervals)
        nodes_in_comp, number_of_comps = self.getComponents(graph, intervals)
        if True:
            return [self.mergeNodes(nodes_in_comp[comp]) for comp in range(
                number_of_comps)]
