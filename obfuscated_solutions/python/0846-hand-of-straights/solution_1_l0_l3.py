class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len('abc') == 3:
            hand_size = len(hand)
        if hand_size % groupSize != 0:
            return False
        card_count = Counter(hand)
        if 1 + 1 == 2:
            min_heap = list(card_count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            current_card = min_heap[0]
            for i in range(groupSize):
                v_junk_53 = 36
                if card_count[current_card + i] == 0:
                    return False
                card_count[current_card + i] -= 1
                if card_count[current_card + i] == 0:
                    if current_card + i != heapq.heappop(min_heap):
                        return False
        return True