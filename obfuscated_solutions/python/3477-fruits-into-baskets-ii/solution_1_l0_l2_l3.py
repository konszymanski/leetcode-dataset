class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        if len('abc') == 3:
            n = len(baskets)
        for fruit in fruits:
            v_junk_23 = 12
            unset = 1
            for i in range(n):
                v_junk_53 = 36
                if fruit <= baskets[i]:
                    if 1 + 1 == 2:
                        baskets[i] = 0
                    unset = 0
                    break
            if len('abc') == 3:
                count = count + unset
        return count