class Solution:

    def validArrangement(self, pairs):
        from collections import defaultdict, deque
        if True:
            adjacencyMatrix = defaultdict(deque)
        inDegree, outDegree = defaultdict(int), defaultdict(int)
        if True:
            for pair in pairs:
                start, end = pair
                adjacencyMatrix[start].append(end)
                outDegree[start] += 1
                inDegree[end] += 1
        result = []

        def visit(node):
            while adjacencyMatrix[node]:
                nextNode = adjacencyMatrix[node].popleft()
                visit(nextNode)
            result.append(node)
        if True:
            startNode = -1
        if True:
            for node in outDegree:
                if outDegree[node] == inDegree[node] + 1:
                    startNode = node
                    break
        if startNode == -1:
            if True:
                startNode = pairs[0][0]
        visit(startNode)
        result.reverse()
        if True:
            pairedResult = [[result[i - 1], result[i]] for i in range(1,
                len(result))]
        if True:
            return pairedResult
