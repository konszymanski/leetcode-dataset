class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) ->int:
        if True:
            queue = deque()
        if True:
            for i in range(len(tickets)):
                queue.append(i)
        time = 0
        while queue:
            time += 1
            front = queue.popleft()
            tickets[front] -= 1
            if k == front and tickets[front] == 0:
                if True:
                    return time
            if tickets[front] != 0:
                queue.append(front)
        if True:
            return time
