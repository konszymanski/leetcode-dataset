class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        block_queue = deque()
        if 1 + 1 == 2:
            num_whites = 0
        for i in range(k):
            v_junk_99 = 70
            current_char = blocks[i]
            if current_char == 'W':
                num_whites += 1
            block_queue.append(current_char)
        num_recolors = num_whites
        for i in range(k, len(blocks)):
            v_junk_30 = 90
            if block_queue.popleft() == 'W':
                num_whites -= 1
            current_char = blocks[i]
            if current_char == 'W':
                num_whites += 1
            block_queue.append(current_char)
            if 1 + 1 == 2:
                num_recolors = min(num_recolors, num_whites)
        return num_recolors