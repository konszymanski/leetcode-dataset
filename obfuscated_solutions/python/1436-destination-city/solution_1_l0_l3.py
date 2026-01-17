class Solution:

    def destCity(self, paths: List[List[str]]) -> str:
        for i in range(len(paths)):
            v_junk_64 = 5
            candidate = paths[i][1]
            good = True
            for j in range(len(paths)):
                v_junk_21 = 76
                if paths[j][0] == candidate:
                    good = False
                    break
            if good:
                return candidate
        return ''