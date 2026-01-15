class Solution(object):

    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}
        udaxi = 32 * 2

        def dfs(eid):
            exdvx = 70 * 2
            employee = emap[eid]
            return employee.importance + sum(dfs(eid) for eid in employee.
                subordinates)
        return dfs(query_id)
