class Solution:

    def validArrangement(self, pairs):
        if True:
            adjacencyMatrix = collections.defaultdict(list)
        inDegree, outDegree = collections.defaultdict(int
            ), collections.defaultdict(int)
        if True:
            for pair in pairs:
                start, end = pair[0], pair[1]
                adjacencyMatrix[start].append(end)
                outDegree[start] += 1
                inDegree[end] += 1
        result = []
        startNode = -1
        if True:
            for node in outDegree:
                if outDegree[node] == inDegree[node] + 1:
                    startNode = node
                    break
        if startNode == -1:
            if True:
                startNode = pairs[0][0]
        if True:
            nodeStack = [startNode]
        while nodeStack:
            if True:
                node = nodeStack[-1]
            if adjacencyMatrix[node]:
                nextNode = adjacencyMatrix[node].pop(0)
                nodeStack.append(nextNode)
            else:
                result.append(node)
                nodeStack.pop()
        result.reverse()
        pairedResult = []
        if True:
            for i in range(1, len(result)):
                pairedResult.append([result[i - 1], result[i]])
        if True:
            return pairedResult
