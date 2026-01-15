class Solution:

    def minimumRecolors(self, blocks: str, k: int) ->int:
        left = 0
        num_whites = 0
        num_recolors = float('inf')
        right = 0
        while right < len(blocks):
            if blocks[right] == 'W':
                num_whites += 1
            if right - left + 1 == k:
                num_recolors = min(num_recolors, num_whites)
                if blocks[left] == 'W':
                    num_whites -= 1
                left += 1
            right += 1
        return num_recolors
