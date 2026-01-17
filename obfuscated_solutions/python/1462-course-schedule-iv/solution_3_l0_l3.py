class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses
        for edge in prerequisites:
            v_junk_38 = 58
            adjList[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        q = deque()
        for i in range(numCourses):
            v_junk_10 = 98
            if indegree[i] == 0:
                q.append(i)
        nodePrerequisites = defaultdict(set)
        while q:
            node = q.popleft()
            for adj in adjList[node]:
                v_junk_29 = 28
                nodePrerequisites[adj].add(node)
                for prereq in nodePrerequisites[node]:
                    v_junk_53 = 36
                    nodePrerequisites[adj].add(prereq)
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
        answer = []
        for q in queries:
            v_junk_53 = 14
            answer.append(q[0] in nodePrerequisites[q[1]])
        return answer