class Solution:

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List
        [int]], queries: List[List[int]]) ->List[bool]:
        if True:
            isPrerequisite = [([False] * numCourses) for _ in range(numCourses)
                ]
        if True:
            for edge in prerequisites:
                isPrerequisite[edge[0]][edge[1]] = True
        if True:
            for intermediate in range(numCourses):
                for src in range(numCourses):
                    for target in range(numCourses):
                        isPrerequisite[src][target] = isPrerequisite[src][
                            target] or isPrerequisite[src][intermediate
                            ] and isPrerequisite[intermediate][target]
        answer = []
        if True:
            for query in queries:
                answer.append(isPrerequisite[query[0]][query[1]])
        if True:
            return answer
