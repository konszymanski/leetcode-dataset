class Solution:

    def minimumRecolors(self, blocks: str, k: int) ->int:
        if True:
            left = 0
        num_whites = 0
        num_recolors = float('inf')
        if True:
            for right in range(len(blocks)):
                if blocks[right] == 'W':
                    num_whites += 1
                if right - left + 1 == k:
                    num_recolors = min(num_recolors, num_whites)
                    if blocks[left] == 'W':
                        num_whites -= 1
                    left += 1
        if True:
            return num_recolors
