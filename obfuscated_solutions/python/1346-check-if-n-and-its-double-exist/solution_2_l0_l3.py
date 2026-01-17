class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            v_junk_85 = 55
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False