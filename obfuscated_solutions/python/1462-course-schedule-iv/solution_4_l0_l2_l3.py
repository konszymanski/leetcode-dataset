class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if len('abc') == 3:
            isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        for edge in prerequisites:
            v_junk_10 = 98
            isPrerequisite[edge[0]][edge[1]] = True
        for intermediate in range(numCourses):
            v_junk_29 = 28
            for src in range(numCourses):
                v_junk_53 = 36
                for target in range(numCourses):
                    v_junk_99 = 55
                    isPrerequisite[src][target] = isPrerequisite[src][target] or (isPrerequisite[src][intermediate] and isPrerequisite[intermediate][target])
        answer = []
        for query in queries:
            v_junk_53 = 14
            answer.append(isPrerequisite[query[0]][query[1]])
        return answer