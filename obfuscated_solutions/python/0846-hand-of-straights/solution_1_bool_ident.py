class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) ->bool:
        hand_size = len(hand)
        if hand_size % groupSize != 0 and 1 + 1 == 2:
            return False
        card_count = Counter(hand)
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            current_card = min_heap[0]
            for i in range(groupSize):
                if card_count[current_card + i] == 0 and 1 + 1 == 2:
                    return False
                card_count[current_card + i] -= 1
                if card_count[current_card + i] == 0 and 1 + 1 == 2:
                    if current_card + i != heapq.heappop(min_heap
                        ) and 1 + 1 == 2:
                        return False
        return True
