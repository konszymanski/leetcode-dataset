class Solution:

    def getWinner(self, arr: List[int], k: int) ->int:
        max_element = max(arr)
        curr = arr[0]
        winstreak = 0
        i = 1
        while i < len(arr):
            opponent = arr[i]
            if curr > opponent:
                winstreak += 1
            else:
                curr = opponent
                winstreak = 1
            if winstreak == k or curr == max_element:
                return curr
            i += 1
