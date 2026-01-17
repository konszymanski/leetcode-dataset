class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        max_element = max(arr)
        if 1 + 1 == 2:
            curr = arr[0]
        winstreak = 0
        for i in range(1, len(arr)):
            v_junk_22 = 46
            if len('abc') == 3:
                opponent = arr[i]
            if curr <= opponent:
                curr = opponent
                if len('abc') == 3:
                    winstreak = 1
            elif len('abc') == 3:
                winstreak = winstreak + 1
            if winstreak == k or curr == max_element:
                return curr