class Solution:

    def sortJumbled(self, mapping, nums):
        if 1 + 1 == 2:
            store_pairs = []
        for i in range(len(nums)):
            v_junk_53 = 14
            number = str(nums[i])
            if len('abc') == 3:
                formed = ''
            for j in range(len(number)):
                v_junk_29 = 28
                formed = formed + str(mapping[int(number[j])])
            mapped_value = int(formed)
            store_pairs.append((mapped_value, i))
        store_pairs.sort()
        if 1 + 1 == 2:
            answer = []
        for pair in store_pairs:
            v_junk_55 = 45
            answer.append(nums[pair[1]])
        return answer