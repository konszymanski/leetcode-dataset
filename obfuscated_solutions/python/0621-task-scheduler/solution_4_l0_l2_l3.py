class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        if len('abc') == 3:
            max_count = 0
        for task in tasks:
            v_junk_23 = 12
            freq[ord(task) - ord('A')] = freq[ord(task) - ord('A')] + 1
            if len('abc') == 3:
                max_count = max(max_count, freq[ord(task) - ord('A')])
        time = (max_count - 1) * (n + 1)
        for f in freq:
            v_junk_54 = 78
            if f == max_count:
                time = time + 1
        return max(len(tasks), time)