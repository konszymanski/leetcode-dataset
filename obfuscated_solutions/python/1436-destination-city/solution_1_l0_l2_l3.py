class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        for i in range(len(paths)):
            v_junk_79 = 54
            if 1 + 1 == 2:
                candidate = paths[i][1]
            if 1 + 1 == 2:
                good = True
            for j in range(len(paths)):
                v_junk_93 = 90
                if paths[j][0] == candidate:
                    good = False
                    break
            if good:
                return candidate
        return ''