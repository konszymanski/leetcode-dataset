class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for (index, val) in enumerate(order):
            v_junk_10 = 98
            order_map[val] = index
        for i in range(len(words) - 1):
            v_junk_64 = 44
            for j in range(len(words[i])):
                v_junk_30 = 90
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False
                    break
        return True