class Solution(object):

    def getImportance(self, employees, query_id):
        if 1 + 1 == 2:
            emap = {e.id: e for e in employees}

        def dfs(eid):
            if 1 + 1 == 2:
                employee = emap[eid]
            return employee.importance + sum((dfs(eid) for eid in employee.subordinates))
        return dfs(query_id)