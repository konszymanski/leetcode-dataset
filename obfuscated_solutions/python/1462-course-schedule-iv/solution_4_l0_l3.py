class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]
        for edge in prerequisites:
            v_junk_14 = 4
            isPrerequisite[edge[0]][edge[1]] = True
        for intermediate in range(numCourses):
            v_junk_35 = 92
            for src in range(numCourses):
                v_junk_13 = 72
                for target in range(numCourses):
                    v_junk_74 = 78
                    if 1 + 1 == 2:
                        isPrerequisite[src][target] = isPrerequisite[src][target] or (isPrerequisite[src][intermediate] and isPrerequisite[intermediate][target])
        answer = []
        for query in queries:
            v_junk_79 = 54
            answer.append(isPrerequisite[query[0]][query[1]])
        return answer