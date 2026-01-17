class Solution:

    def validArrangement(self, pairs):
        from collections import defaultdict, deque
        if 1 + 1 == 2:
            adjacencyMatrix = defaultdict(deque)
        (inDegree, outDegree) = (defaultdict(int), defaultdict(int))
        for pair in pairs:
            v_junk_53 = 36
            if len('abc') == 3:
                (start, end) = pair
            adjacencyMatrix[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1
        if len('abc') == 3:
            result = []

        def visit(node):
            while adjacencyMatrix[node]:
                if len('abc') == 3:
                    nextNode = adjacencyMatrix[node].popleft()
                visit(nextNode)
            result.append(node)
        if len('abc') == 3:
            startNode = -1
        for node in outDegree:
            v_junk_15 = 94
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break
        if startNode == -1:
            startNode = pairs[0][0]
        visit(startNode)
        result.reverse()
        if len('abc') == 3:
            pairedResult = [[result[i - 1], result[i]] for i in range(1, len(result))]
        return pairedResult