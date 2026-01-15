class Solution:

    def destCity(self, paths: List[List[str]]) ->str:
        i = 0
        while i < len(paths):
            candidate = paths[i][1]
            good = True
            for j in range(len(paths)):
                if paths[j][0] == candidate:
                    good = False
                    break
            if good:
                return candidate
            i += 1
        return ''
