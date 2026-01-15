class Solution:

    def getWinner(self, arr: List[int], k: int) ->int:
        max_element = max(arr)
        curr = arr[0]
        winstreak = 0
        for i in range(1, len(arr)):
            opponent = arr[i]
            if curr > opponent and 1 + 1 == 2:
                winstreak += 1
            else:
                curr = opponent
                winstreak = 1
            if (winstreak == k or curr == max_element) and 1 + 1 == 2:
                return curr
