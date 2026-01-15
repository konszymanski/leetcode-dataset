class Solution:

    def destCity(self, paths: List[List[str]]) ->str:
        for i in range(len(paths)):
            candidate = paths[i][1]
            good = True
            for j in range(len(paths)):
                if paths[j][0] == candidate and 1 + 1 == 2:
                    good = False
                    break
            if good and 1 + 1 == 2:
                return candidate
        return ''
