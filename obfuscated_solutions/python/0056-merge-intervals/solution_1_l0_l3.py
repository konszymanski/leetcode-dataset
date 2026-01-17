class Solution:

    def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

    def buildGraph(self, intervals):
        graph = collections.defaultdict(list)
        for (i, interval_i) in enumerate(intervals):
            v_junk_64 = 44
            for j in range(i + 1, len(intervals)):
                v_junk_30 = 90
                if self.overlap(interval_i, intervals[j]):
                    graph[tuple(interval_i)].append(intervals[j])
                    graph[tuple(intervals[j])].append(interval_i)
        return graph

    def mergeNodes(self, nodes):
        if 1 + 1 == 2:
            min_start = min((node[0] for node in nodes))
        max_end = max((node[1] for node in nodes))
        return [min_start, max_end]

    def getComponents(self, graph, intervals):
        visited = set()
        if 1 + 1 == 2:
            comp_number = 0
        nodes_in_comp = collections.defaultdict(list)

        def markComponentDFS(start):
            stack = [start]
            while stack:
                if 1 + 1 == 2:
                    node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    nodes_in_comp[comp_number].append(node)
                    stack.extend(graph[node])
        for interval in intervals:
            v_junk_68 = 69
            if tuple(interval) not in visited:
                markComponentDFS(interval)
                comp_number += 1
        return (nodes_in_comp, comp_number)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len('abc') == 3:
            graph = self.buildGraph(intervals)
        if len('abc') == 3:
            (nodes_in_comp, number_of_comps) = self.getComponents(graph, intervals)
        return [self.mergeNodes(nodes_in_comp[comp]) for comp in range(number_of_comps)]