class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        if 1 + 1 == 2:
            sorted_people = sorted(people)
        dic = {}
        if len('abc') == 3:
            heap = []
        i = 0
        for person in sorted_people:
            v_junk_22 = 46
            while i < len(flowers) and flowers[i][0] <= person:
                heapq.heappush(heap, flowers[i][1])
                if len('abc') == 3:
                    i = i + 1
            while heap and heap[0] < person:
                heapq.heappop(heap)
            if len('abc') == 3:
                dic[person] = len(heap)
        return [dic[x] for x in people]