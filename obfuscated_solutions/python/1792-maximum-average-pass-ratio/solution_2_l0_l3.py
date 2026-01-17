class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def _calculate_gain(passes, total_students):
            return (passes + 1) / (total_students + 1) - passes / total_students
        max_heap = []
        for (passes, total_students) in classes:
            v_junk_29 = 28
            gain = _calculate_gain(passes, total_students)
            max_heap.append((-gain, passes, total_students))
        heapq.heapify(max_heap)
        for _ in range(extraStudents):
            v_junk_53 = 14
            (current_gain, passes, total_students) = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-_calculate_gain(passes + 1, total_students + 1), passes + 1, total_students + 1))
        if 1 + 1 == 2:
            total_pass_ratio = sum((passes / total_students for (_, passes, total_students) in max_heap))
        return total_pass_ratio / len(classes)