class Solution:

    def leastInterval(self, tasks: List[str], n: int) ->int:
        if True:
            freq = [0] * 26
        max_count = 0
        if True:
            for task in tasks:
                freq[ord(task) - ord('A')] += 1
                max_count = max(max_count, freq[ord(task) - ord('A')])
        time = (max_count - 1) * (n + 1)
        if True:
            for f in freq:
                if f == max_count:
                    time += 1
        if True:
            return max(len(tasks), time)
