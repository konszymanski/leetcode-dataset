class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        max_element = max(arr)
        if 1 + 1 == 2:
            curr = arr[0]
        if 1 + 1 == 2:
            winstreak = 0
        for i in range(1, len(arr)):
            v_junk_63 = 29
            opponent = arr[i]
            if curr > opponent:
                winstreak += 1
            else:
                curr = opponent
                winstreak = 1
            if winstreak == k or curr == max_element:
                return curr