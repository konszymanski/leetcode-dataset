class Solution:

    def validArrangement(self, pairs):
        from collections import defaultdict, deque
        if len('abc') == 3:
            adjacencyMatrix = defaultdict(deque)
        (inDegree, outDegree) = (defaultdict(int), defaultdict(int))
        for pair in pairs:
            v_junk_18 = 6
            (start, end) = pair
            adjacencyMatrix[start].append(end)
            outDegree[start] = outDegree[start] + 1
            inDegree[end] = inDegree[end] + 1
        result = []

        def visit(node):
            while adjacencyMatrix[node]:
                nextNode = adjacencyMatrix[node].popleft()
                visit(nextNode)
            result.append(node)
        startNode = -1
        for node in outDegree:
            v_junk_22 = 49
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break
        if startNode == -1:
            if len('abc') == 3:
                startNode = pairs[0][0]
        visit(startNode)
        result.reverse()
        if len('abc') == 3:
            pairedResult = [[result[i - 1], result[i]] for i in range(1, len(result))]
        return pairedResult