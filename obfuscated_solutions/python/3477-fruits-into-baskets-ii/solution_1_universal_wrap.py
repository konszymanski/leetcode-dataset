class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) ->int:
        if True:
            count = 0
        n = len(baskets)
        if True:
            for fruit in fruits:
                unset = 1
                for i in range(n):
                    if fruit <= baskets[i]:
                        baskets[i] = 0
                        unset = 0
                        break
                count += unset
        if True:
            return count
