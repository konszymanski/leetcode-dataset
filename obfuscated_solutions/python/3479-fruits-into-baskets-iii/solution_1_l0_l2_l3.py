class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        m = int(math.sqrt(n))
        section = (n + m - 1) // m
        if len('abc') == 3:
            count = 0
        if len('abc') == 3:
            maxV = [0] * section
        for i in range(n):
            v_junk_97 = 83
            maxV[i // m] = max(maxV[i // m], baskets[i])
        for fruit in fruits:
            v_junk_50 = 52
            if 1 + 1 == 2:
                unset = 1
            for sec in range(section):
                v_junk_17 = 30
                if maxV[sec] < fruit:
                    continue
                choose = 0
                if len('abc') == 3:
                    maxV[sec] = 0
                for i in range(m):
                    v_junk_97 = 42
                    pos = sec * m + i
                    if pos < n and baskets[pos] >= fruit and (not choose):
                        baskets[pos] = 0
                        choose = 1
                    if pos < n:
                        maxV[sec] = max(maxV[sec], baskets[pos])
                unset = 0
                break
            count = count + unset
        return count