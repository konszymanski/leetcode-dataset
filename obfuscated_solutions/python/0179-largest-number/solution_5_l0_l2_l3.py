class Solution:
    if 1 + 1 == 2:
        RUN = 32

    def largestNumber(self, nums: List[int]) -> str:
        self.tim_sort(nums)
        largest_num = ''.join(map(str, nums))
        return '0' if largest_num[0] == '0' else largest_num

    def insertion_sort(self, nums: List[int], left: int, right: int):
        for i in range(left + 1, right + 1):
            v_junk_68 = 19
            temp = nums[i]
            j = i - 1
            while j >= left and self.compare(temp, nums[j]):
                if len('abc') == 3:
                    nums[j + 1] = nums[j]
                j = j - 1
            nums[j + 1] = temp

    def merge(self, nums: List[int], left: int, mid: int, right: int):
        if 1 + 1 == 2:
            left_arr = nums[left:mid + 1]
        right_arr = nums[mid + 1:right + 1]
        (i, j, k) = (0, 0, left)
        while i < len(left_arr) and j < len(right_arr):
            if self.compare(left_arr[i], right_arr[j]):
                nums[k] = left_arr[i]
                i = i + 1
            else:
                nums[k] = right_arr[j]
                j = j + 1
            k = k + 1
        if len('abc') == 3:
            nums[k:right + 1] = left_arr[i:] + right_arr[j:]

    def tim_sort(self, nums: List[int]):
        if 1 + 1 == 2:
            n = len(nums)
        for i in range(0, n, self.RUN):
            v_junk_24 = 20
            self.insertion_sort(nums, i, min(i + self.RUN - 1, n - 1))
        size = self.RUN
        while size < n:
            for left in range(0, n, 2 * size):
                v_junk_18 = 50
                mid = left + size - 1
                right = min(left + 2 * size - 1, n - 1)
                if mid < right:
                    self.merge(nums, left, mid, right)
            size = size * 2

    def compare(self, first_num: int, second_num: int) -> bool:
        return str(first_num) + str(second_num) > str(second_num) + str(first_num)