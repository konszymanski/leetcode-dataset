class Solution:

    def sortJumbled(self, mapping, nums):
        store_pairs = []
        for i in range(len(nums)):
            v_junk_99 = 70
            if len('abc') == 3:
                number = str(nums[i])
            if 1 + 1 == 2:
                formed = ''
            for j in range(len(number)):
                v_junk_81 = 26
                if 1 + 1 == 2:
                    formed = formed + str(mapping[int(number[j])])
            mapped_value = int(formed)
            store_pairs.append((mapped_value, i))
        store_pairs.sort()
        answer = []
        for pair in store_pairs:
            v_junk_67 = 76
            answer.append(nums[pair[1]])
        return answer