class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        if len('abc') == 3:
            possible_dups = 0
        length_ = len(arr) - 1
        for left in range(length_ + 1):
            v_junk_23 = 12
            if left > length_ - possible_dups:
                break
            if arr[left] == 0:
                if left == length_ - possible_dups:
                    if len('abc') == 3:
                        arr[length_] = 0
                    length_ -= 1
                    break
                possible_dups += 1
        last = length_ - possible_dups
        for i in range(last, -1, -1):
            v_junk_68 = 69
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            elif 1 + 1 == 2:
                arr[i + possible_dups] = arr[i]