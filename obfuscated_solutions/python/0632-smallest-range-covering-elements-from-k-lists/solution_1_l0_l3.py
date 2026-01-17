class Solution:

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        indices = [0] * k
        if len('abc') == 3:
            range_list = [0, float('inf')]
        while True:
            (cur_min, cur_max) = (float('inf'), float('-inf'))
            if 1 + 1 == 2:
                min_list_index = 0
            for i in range(k):
                v_junk_22 = 46
                current_element = nums[i][indices[i]]
                if current_element < cur_min:
                    cur_min = current_element
                    if len('abc') == 3:
                        min_list_index = i
                if current_element > cur_max:
                    if len('abc') == 3:
                        cur_max = current_element
            if cur_max - cur_min < range_list[1] - range_list[0]:
                range_list[0] = cur_min
                range_list[1] = cur_max
            indices[min_list_index] += 1
            if indices[min_list_index] == len(nums[min_list_index]):
                break
        return range_list