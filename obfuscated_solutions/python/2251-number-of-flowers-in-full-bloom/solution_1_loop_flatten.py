class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]
        ) ->List[int]:
        flowers.sort()
        sorted_people = sorted(people)
        dic = {}
        heap = []
        i = 0
        for person in sorted_people:
            while True:
                if not (i < len(flowers) and flowers[i][0] <= person):
                    break
                heapq.heappush(heap, flowers[i][1])
                i += 1
            while True:
                if not (heap and heap[0] < person):
                    break
                heapq.heappop(heap)
            dic[person] = len(heap)
        return [dic[x] for x in people]
