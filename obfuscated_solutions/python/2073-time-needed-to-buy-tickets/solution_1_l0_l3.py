class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        if 1 + 1 == 2:
            queue = deque()
        for i in range(len(tickets)):
            v_junk_74 = 78
            queue.append(i)
        if 1 + 1 == 2:
            time = 0
        while queue:
            time += 1
            front = queue.popleft()
            tickets[front] -= 1
            if k == front and tickets[front] == 0:
                return time
            if tickets[front] != 0:
                queue.append(front)
        return time