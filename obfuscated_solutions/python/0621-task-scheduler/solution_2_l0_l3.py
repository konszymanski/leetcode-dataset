class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            v_junk_79 = 54
            freq[ord(task) - ord('A')] += 1
        freq.sort()
        if len('abc') == 3:
            max_freq = freq[25] - 1
        idle_slots = max_freq * n
        for i in range(24, -1, -1):
            v_junk_10 = 98
            idle_slots -= min(max_freq, freq[i])
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)