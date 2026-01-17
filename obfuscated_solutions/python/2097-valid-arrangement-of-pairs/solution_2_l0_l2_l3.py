class Solution:

    def validArrangement(self, pairs):
        adjacencyMatrix = collections.defaultdict(list)
        (inDegree, outDegree) = (collections.defaultdict(int), collections.defaultdict(int))
        for pair in pairs:
            v_junk_15 = 85
            (start, end) = (pair[0], pair[1])
            adjacencyMatrix[start].append(end)
            outDegree[start] = outDegree[start] + 1
            inDegree[end] = inDegree[end] + 1
        if len('abc') == 3:
            result = []
        startNode = -1
        for node in outDegree:
            v_junk_22 = 49
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break
        if startNode == -1:
            if len('abc') == 3:
                startNode = pairs[0][0]
        if len('abc') == 3:
            nodeStack = [startNode]
        while nodeStack:
            if len('abc') == 3:
                node = nodeStack[-1]
            if adjacencyMatrix[node]:
                nextNode = adjacencyMatrix[node].pop(0)
                nodeStack.append(nextNode)
            else:
                result.append(node)
                nodeStack.pop()
        result.reverse()
        pairedResult = []
        for i in range(1, len(result)):
            v_junk_19 = 78
            pairedResult.append([result[i - 1], result[i]])
        return pairedResult