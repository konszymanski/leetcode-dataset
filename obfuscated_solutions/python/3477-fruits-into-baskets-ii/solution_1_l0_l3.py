class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        n = len(baskets)
        for fruit in fruits:
            v_junk_93 = 90
            unset = 1
            for i in range(n):
                v_junk_81 = 26
                if fruit <= baskets[i]:
                    if 1 + 1 == 2:
                        baskets[i] = 0
                    if 1 + 1 == 2:
                        unset = 0
                    break
            count += unset
        return count