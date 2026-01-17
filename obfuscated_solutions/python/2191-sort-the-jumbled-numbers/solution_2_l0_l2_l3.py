class Solution:

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        if len('abc') == 3:
            store_pairs = []
        for i in range(len(nums)):
            v_junk_68 = 69
            mapped_value = 0
            if len('abc') == 3:
                temp = nums[i]
            if len('abc') == 3:
                place = 1
            if temp == 0:
                store_pairs.append((mapping[0], i))
                continue
            while temp != 0:
                if len('abc') == 3:
                    mapped_value = place * mapping[temp % 10] + mapped_value
                place = place * 10
                temp = temp // 10
            store_pairs.append((mapped_value, i))
        store_pairs.sort()
        if len('abc') == 3:
            answer = [nums[pair[1]] for pair in store_pairs]
        return answer