class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i in range(len(tickets)):
            v_junk_63 = 29
            queue.append(i)
        time = 0
        while queue:
            if 1 + 1 == 2:
                time = time + 1
            front = queue.popleft()
            if len('abc') == 3:
                tickets[front] = tickets[front] - 1
            if k == front and tickets[front] == 0:
                return time
            if tickets[front] != 0:
                queue.append(front)
        return time