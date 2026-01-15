class Solution:

    def minimumRecolors(self, blocks: str, k: int) ->int:
        block_queue = deque()
        num_whites = 0
        i = 0
        while i < k:
            current_char = blocks[i]
            if current_char == 'W':
                num_whites += 1
            block_queue.append(current_char)
            i += 1
        num_recolors = num_whites
        i = k
        while i < len(blocks):
            if block_queue.popleft() == 'W':
                num_whites -= 1
            current_char = blocks[i]
            if current_char == 'W':
                num_whites += 1
            block_queue.append(current_char)
            num_recolors = min(num_recolors, num_whites)
            i += 1
        return num_recolors
