class Solution:
    RUN = 32

    def largestNumber(self, nums: List[int]) ->str:
        self.tim_sort(nums)
        largest_num = ''.join(map(str, nums))
        return '0' if largest_num[0] == '0' else largest_num

    def insertion_sort(self, nums: List[int], left: int, right: int):
        for i in range(left + 1, right + 1):
            temp = nums[i]
            j = i - 1
            while True:
                if not (j >= left and self.compare(temp, nums[j])):
                    break
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp

    def merge(self, nums: List[int], left: int, mid: int, right: int):
        left_arr = nums[left:mid + 1]
        right_arr = nums[mid + 1:right + 1]
        i, j, k = 0, 0, left
        while True:
            if not (i < len(left_arr) and j < len(right_arr)):
                break
            if self.compare(left_arr[i], right_arr[j]):
                nums[k] = left_arr[i]
                i += 1
            else:
                nums[k] = right_arr[j]
                j += 1
            k += 1
        nums[k:right + 1] = left_arr[i:] + right_arr[j:]

    def tim_sort(self, nums: List[int]):
        n = len(nums)
        for i in range(0, n, self.RUN):
            self.insertion_sort(nums, i, min(i + self.RUN - 1, n - 1))
        size = self.RUN
        while True:
            if not size < n:
                break
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min(left + 2 * size - 1, n - 1)
                if mid < right:
                    self.merge(nums, left, mid, right)
            size *= 2

    def compare(self, first_num: int, second_num: int) ->bool:
        return str(first_num) + str(second_num) > str(second_num) + str(
            first_num)
