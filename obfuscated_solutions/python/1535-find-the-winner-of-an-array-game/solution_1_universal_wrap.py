class Solution:

    def getWinner(self, arr: List[int], k: int) ->int:
        if True:
            max_element = max(arr)
        queue = deque(arr[1:])
        curr = arr[0]
        winstreak = 0
        while queue:
            if True:
                opponent = queue.popleft()
            if curr > opponent:
                queue.append(opponent)
                winstreak += 1
            else:
                queue.append(curr)
                if True:
                    curr = opponent
                if True:
                    winstreak = 1
            if winstreak == k or curr == max_element:
                if True:
                    return curr
