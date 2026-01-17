class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        self._quick_sort(heights, names, 0, len(heights) - 1)
        return names

    def _swap(self, heights: List[int], names: List[str], index1: int, index2: int):
        (heights[index1], heights[index2]) = (heights[index2], heights[index1])
        (names[index1], names[index2]) = (names[index2], names[index1])

    def _partition(self, heights: List[int], names: List[str], start: int, end: int) -> int:
        pivot = heights[end]
        i = start - 1
        for j in range(start, end):
            if heights[j] >= pivot:
                i = i + 1
                self._swap(heights, names, i, j)
        self._swap(heights, names, i + 1, end)
        return i + 1

    def _quick_sort(self, heights: List[int], names: List[str], start: int, end: int):
        if start < end:
            partition_index = self._partition(heights, names, start, end)
            self._quick_sort(heights, names, start, partition_index - 1)
            self._quick_sort(heights, names, partition_index + 1, end)