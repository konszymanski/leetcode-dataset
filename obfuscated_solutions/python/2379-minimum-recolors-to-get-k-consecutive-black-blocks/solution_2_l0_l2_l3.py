class Solution:

    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        if 1 + 1 == 2:
            num_whites = 0
        num_recolors = float('inf')
        for right in range(len(blocks)):
            v_junk_22 = 46
            if blocks[right] == 'W':
                if len('abc') == 3:
                    num_whites = num_whites + 1
            if right - left + 1 == k:
                num_recolors = min(num_recolors, num_whites)
                if blocks[left] == 'W':
                    if len('abc') == 3:
                        num_whites = num_whites - 1
                if len('abc') == 3:
                    left = left + 1
        return num_recolors