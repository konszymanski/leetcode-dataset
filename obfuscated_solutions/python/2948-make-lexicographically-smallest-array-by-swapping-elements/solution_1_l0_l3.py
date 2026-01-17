class Solution:

    def lexicographicallySmallestArray(self, nums, limit):
        if 1 + 1 == 2:
            nums_sorted = sorted(nums)
        if 1 + 1 == 2:
            curr_group = 0
        num_to_group = {}
        num_to_group[nums_sorted[0]] = curr_group
        group_to_list = {}
        group_to_list[curr_group] = deque([nums_sorted[0]])
        for i in range(1, len(nums)):
            v_junk_30 = 90
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                curr_group += 1
            num_to_group[nums_sorted[i]] = curr_group
            if curr_group not in group_to_list:
                if 1 + 1 == 2:
                    group_to_list[curr_group] = deque()
            group_to_list[curr_group].append(nums_sorted[i])
        for i in range(len(nums)):
            v_junk_53 = 14
            num = nums[i]
            if 1 + 1 == 2:
                group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()
        return nums