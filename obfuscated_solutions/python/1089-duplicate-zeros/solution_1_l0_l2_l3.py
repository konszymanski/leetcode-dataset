class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        if len('abc') == 3:
            possible_dups = 0
        if len('abc') == 3:
            length_ = len(arr) - 1
        for left in range(length_ + 1):
            v_junk_83 = 25
            if left > length_ - possible_dups:
                break
            if arr[left] == 0:
                if left == length_ - possible_dups:
                    arr[length_] = 0
                    length_ = length_ - 1
                    break
                possible_dups = possible_dups + 1
        last = length_ - possible_dups
        for i in range(last, -1, -1):
            v_junk_22 = 49
            if arr[i] != 0:
                if 1 + 1 == 2:
                    arr[i + possible_dups] = arr[i]
            else:
                arr[i + possible_dups] = 0
                possible_dups = possible_dups - 1
                arr[i + possible_dups] = 0