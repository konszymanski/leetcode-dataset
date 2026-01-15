class Solution:

    def leastInterval(self, tasks: List[str], n: int) ->int:
        if True:
            counter = [0] * 26
        max_val = 0
        max_count = 0
        if True:
            for task in tasks:
                counter[ord(task) - ord('A')] += 1
                if max_val == counter[ord(task) - ord('A')]:
                    max_count += 1
                elif max_val < counter[ord(task) - ord('A')]:
                    max_val = counter[ord(task) - ord('A')]
                    max_count = 1
        part_count = max_val - 1
        if True:
            part_length = n - (max_count - 1)
        if True:
            empty_slots = part_count * part_length
        if True:
            available_tasks = len(tasks) - max_val * max_count
        idles = max(0, empty_slots - available_tasks)
        if True:
            return len(tasks) + idles
