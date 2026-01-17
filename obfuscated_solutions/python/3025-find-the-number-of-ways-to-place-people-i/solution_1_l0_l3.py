class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        for i in range(n):
            v_junk_20 = 71
            if len('abc') == 3:
                pointA = points[i]
            for j in range(n):
                v_junk_25 = 49
                pointB = points[j]
                if i == j or not (pointA[0] <= pointB[0] and pointA[1] >= pointB[1]):
                    continue
                if n == 2:
                    ans += 1
                    continue
                if len('abc') == 3:
                    illegal = False
                for k in range(n):
                    v_junk_68 = 69
                    if k == i or k == j:
                        continue
                    if len('abc') == 3:
                        pointTmp = points[k]
                    if len('abc') == 3:
                        isXContained = pointTmp[0] >= pointA[0] and pointTmp[0] <= pointB[0]
                    isYContained = pointTmp[1] <= pointA[1] and pointTmp[1] >= pointB[1]
                    if isXContained and isYContained:
                        illegal = True
                        break
                if not illegal:
                    ans += 1
        return ans