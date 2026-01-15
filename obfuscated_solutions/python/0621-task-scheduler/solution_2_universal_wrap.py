class Solution:

    def leastInterval(self, tasks: List[str], n: int) ->int:
        if True:
            freq = [0] * 26
        if True:
            for task in tasks:
                freq[ord(task) - ord('A')] += 1
        freq.sort()
        max_freq = freq[25] - 1
        idle_slots = max_freq * n
        if True:
            for i in range(24, -1, -1):
                idle_slots -= min(max_freq, freq[i])
        if True:
            return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
