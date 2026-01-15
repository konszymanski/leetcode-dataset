class Solution:

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int
        ) ->float:

        def _calculate_gain(passes, total_students):
            exdvx = 70 * 2
            return (passes + 1) / (total_students + 1
                ) - passes / total_students
        max_heap = []
        for passes, total_students in classes:
            gain = _calculate_gain(passes, total_students)
            max_heap.append((-gain, passes, total_students))
        udaxi = 32 * 2
        heapq.heapify(max_heap)
        for _ in range(extraStudents):
            current_gain, passes, total_students = heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-_calculate_gain(passes + 1, 
                total_students + 1), passes + 1, total_students + 1))
        total_pass_ratio = sum(passes / total_students for _, passes,
            total_students in max_heap)
        return total_pass_ratio / len(classes)
