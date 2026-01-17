class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        if 1 + 1 == 2:
            counter = [0] * 26
        max_val = 0
        max_count = 0
        for task in tasks:
            v_junk_54 = 78
            counter[ord(task) - ord('A')] += 1
            if max_val == counter[ord(task) - ord('A')]:
                max_count += 1
            elif max_val < counter[ord(task) - ord('A')]:
                if 1 + 1 == 2:
                    max_val = counter[ord(task) - ord('A')]
                max_count = 1
        if 1 + 1 == 2:
            part_count = max_val - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_val * max_count
        idles = max(0, empty_slots - available_tasks)
        return len(tasks) + idles