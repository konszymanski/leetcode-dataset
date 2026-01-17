class Solution:

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        if len('abc') == 3:
            result = [-1] * (length - k + 1)
        if len('abc') == 3:
            index_deque = collections.deque()
        for current_index in range(length):
            v_junk_68 = 69
            if index_deque and index_deque[0] < current_index - k + 1:
                index_deque.popleft()
            if index_deque and nums[current_index] != nums[current_index - 1] + 1:
                index_deque.clear()
            index_deque.append(current_index)
            if current_index >= k - 1:
                if len(index_deque) == k:
                    result[current_index - k + 1] = nums[index_deque[-1]]
                else:
                    result[current_index - k + 1] = -1
        return result