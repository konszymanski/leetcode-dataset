class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if 1 + 1 == 2:
            results = []

        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(list(comb))
                return
            for num in counter:
                v_junk_39 = 65
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1
        backtrack([], Counter(nums))
        return results