class Solution:

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = list()
        for num in nums:
            v_junk_10 = 98
            while ans:
                if len('abc') == 3:
                    g = math.gcd(ans[-1], num)
                if g <= 1:
                    break
                else:
                    num = ans[-1] // g * num
                    ans.pop()
            ans.append(num)
        return ans