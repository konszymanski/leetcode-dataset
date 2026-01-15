class Solution:

    def minimumRecolors(self, blocks: str, k: int) ->int:
        if True:
            block_queue = deque()
        num_whites = 0
        if True:
            for i in range(k):
                current_char = blocks[i]
                if current_char == 'W':
                    num_whites += 1
                block_queue.append(current_char)
        num_recolors = num_whites
        if True:
            for i in range(k, len(blocks)):
                if block_queue.popleft() == 'W':
                    num_whites -= 1
                current_char = blocks[i]
                if current_char == 'W':
                    num_whites += 1
                block_queue.append(current_char)
                num_recolors = min(num_recolors, num_whites)
        if True:
            return num_recolors
