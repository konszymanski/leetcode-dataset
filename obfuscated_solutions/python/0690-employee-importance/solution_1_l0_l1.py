class Solution(object):
    def getImportance(self, employees, query_id):
        v1_754 = {v2_214.id: v2_214 for v2_214 in employees}
        def v3_125(v4_859):
            v5_381 = v1_754[v4_859]
            return (v5_381.v6_350 +
                    sum(v3_125(v4_859) for v4_859 in v5_381.v7_328))
        return v3_125(query_id)
