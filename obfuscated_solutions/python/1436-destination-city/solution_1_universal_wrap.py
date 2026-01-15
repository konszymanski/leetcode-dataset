class Solution:

    def destCity(self, paths: List[List[str]]) ->str:
        if True:
            for i in range(len(paths)):
                candidate = paths[i][1]
                good = True
                for j in range(len(paths)):
                    if paths[j][0] == candidate:
                        good = False
                        break
                if good:
                    return candidate
        if True:
            return ''
