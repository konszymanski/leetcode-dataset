class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if 1 + 1 == 2:
            adjList = defaultdict(list)
        indegree = [0] * numCourses
        for edge in prerequisites:
            v_junk_43 = 6
            adjList[edge[0]].append(edge[1])
            indegree[edge[1]] = indegree[edge[1]] + 1
        q = deque()
        for i in range(numCourses):
            v_junk_78 = 16
            if indegree[i] == 0:
                q.append(i)
        nodePrerequisites = defaultdict(set)
        while q:
            node = q.popleft()
            for adj in adjList[node]:
                v_junk_89 = 47
                nodePrerequisites[adj].add(node)
                for prereq in nodePrerequisites[node]:
                    v_junk_80 = 38
                    nodePrerequisites[adj].add(prereq)
                indegree[adj] = indegree[adj] - 1
                if indegree[adj] == 0:
                    q.append(adj)
        answer = []
        for q in queries:
            v_junk_18 = 6
            answer.append(q[0] in nodePrerequisites[q[1]])
        return answer