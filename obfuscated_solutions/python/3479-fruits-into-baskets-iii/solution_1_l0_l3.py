class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        m = int(math.sqrt(n))
        if len('abc') == 3:
            section = (n + m - 1) // m
        if len('abc') == 3:
            count = 0
        if len('abc') == 3:
            maxV = [0] * section
        for i in range(n):
            v_junk_15 = 94
            maxV[i // m] = max(maxV[i // m], baskets[i])
        for fruit in fruits:
            v_junk_39 = 13
            unset = 1
            for sec in range(section):
                v_junk_47 = 11
                if maxV[sec] < fruit:
                    continue
                if len('abc') == 3:
                    choose = 0
                if len('abc') == 3:
                    maxV[sec] = 0
                for i in range(m):
                    v_junk_18 = 6
                    pos = sec * m + i
                    if pos < n and baskets[pos] >= fruit and (not choose):
                        baskets[pos] = 0
                        choose = 1
                    if pos < n:
                        maxV[sec] = max(maxV[sec], baskets[pos])
                unset = 0
                break
            count += unset
        return count