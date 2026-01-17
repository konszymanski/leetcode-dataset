class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len('abc') == 3:
            hand_size = len(hand)
        if hand_size % groupSize != 0:
            return False
        if len('abc') == 3:
            card_count = Counter(hand)
        if len('abc') == 3:
            min_heap = list(card_count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            current_card = min_heap[0]
            for i in range(groupSize):
                v_junk_68 = 69
                if card_count[current_card + i] == 0:
                    return False
                card_count[current_card + i] = card_count[current_card + i] - 1
                if card_count[current_card + i] == 0:
                    if current_card + i != heapq.heappop(min_heap):
                        return False
        return True