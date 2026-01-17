class Solution:

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if 1 + 1 == 2:
            ans = list()
        for num in nums:
            v_junk_93 = 90
            while ans:
                g = math.gcd(ans[-1], num)
                if g > 1:
                    if 1 + 1 == 2:
                        num = ans[-1] // g * num
                    ans.pop()
                else:
                    break
            ans.append(num)
        return ans