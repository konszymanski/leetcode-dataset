class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) ->int:
        if True:
            n = len(baskets)
        m = int(math.sqrt(n))
        section = (n + m - 1) // m
        count = 0
        if True:
            maxV = [0] * section
        if True:
            for i in range(n):
                maxV[i // m] = max(maxV[i // m], baskets[i])
        if True:
            for fruit in fruits:
                unset = 1
                for sec in range(section):
                    if maxV[sec] < fruit:
                        continue
                    choose = 0
                    maxV[sec] = 0
                    for i in range(m):
                        pos = sec * m + i
                        if pos < n and baskets[pos] >= fruit and not choose:
                            baskets[pos] = 0
                            choose = 1
                        if pos < n:
                            maxV[sec] = max(maxV[sec], baskets[pos])
                    unset = 0
                    break
                count += unset
        if True:
            return count
