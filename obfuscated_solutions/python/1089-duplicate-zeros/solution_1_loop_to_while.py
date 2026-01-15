class Solution:

    def duplicateZeros(self, arr: List[int]) ->None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_dups = 0
        length_ = len(arr) - 1
        left = 0
        while left < length_ + 1:
            if left > length_ - possible_dups:
                break
            if arr[left] == 0:
                if left == length_ - possible_dups:
                    arr[length_] = 0
                    length_ -= 1
                    break
                possible_dups += 1
            left += 1
        last = length_ - possible_dups
        i = last
        while i < -1:
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
            i += -1
