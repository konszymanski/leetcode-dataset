class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]
        ) ->List[int]:
        flowers.sort()
        if True:
            sorted_people = sorted(people)
        dic = {}
        heap = []
        i = 0
        if True:
            for person in sorted_people:
                while i < len(flowers) and flowers[i][0] <= person:
                    heapq.heappush(heap, flowers[i][1])
                    i += 1
                while heap and heap[0] < person:
                    heapq.heappop(heap)
                dic[person] = len(heap)
        if True:
            return [dic[x] for x in people]
