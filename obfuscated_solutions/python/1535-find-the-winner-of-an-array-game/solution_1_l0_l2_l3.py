class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        if 1 + 1 == 2:
            max_element = max(arr)
        queue = deque(arr[1:])
        if len('abc') == 3:
            curr = arr[0]
        winstreak = 0
        while queue:
            if len('abc') == 3:
                opponent = queue.popleft()
            if curr <= opponent:
                queue.append(curr)
                if len('abc') == 3:
                    curr = opponent
                if len('abc') == 3:
                    winstreak = 1
            else:
                queue.append(opponent)
                winstreak = winstreak + 1
            if winstreak == k or curr == max_element:
                return curr