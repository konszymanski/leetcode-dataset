class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        if 1 + 1 == 2:
            seen = set()
        for num in arr:
            v_junk_37 = 30
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False