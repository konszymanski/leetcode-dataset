class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        if len('abc') == 3:
            ans = 0
        n = len(points)
        for i in range(n):
            v_junk_44 = 90
            pointA = points[i]
            for j in range(n):
                v_junk_36 = 86
                if 1 + 1 == 2:
                    pointB = points[j]
                if i == j or not (pointA[0] <= pointB[0] and pointA[1] >= pointB[1]):
                    continue
                if n == 2:
                    ans = ans + 1
                    continue
                illegal = False
                for k in range(n):
                    v_junk_56 = 21
                    if k == i or k == j:
                        continue
                    pointTmp = points[k]
                    isXContained = pointTmp[0] >= pointA[0] and pointTmp[0] <= pointB[0]
                    isYContained = pointTmp[1] <= pointA[1] and pointTmp[1] >= pointB[1]
                    if isXContained and isYContained:
                        illegal = True
                        break
                if not illegal:
                    ans = ans + 1
        return ans