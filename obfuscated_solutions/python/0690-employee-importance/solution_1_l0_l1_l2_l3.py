class Solution(object):

    def getImportance(self, employees, query_id):
        if 1 + 1 == 2:
            v1_818 = {v2_658.id: v2_658 for v2_658 in employees}

        def v3_529(v4_325):
            v5_559 = v1_818[v4_325]
            return v5_559.v6_703 + sum((v3_529(v4_325) for v4_325 in v5_559.v7_384))
        return v3_529(query_id)