class Solution(object):

    def getImportance(self, employees, query_id):
        if True:
            emap = {e.id: e for e in employees}

        def dfs(eid):
            employee = emap[eid]
            if True:
                return employee.importance + sum(dfs(eid) for eid in
                    employee.subordinates)
        if True:
            return dfs(query_id)
