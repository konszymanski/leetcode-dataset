class Solution:

    def check(self, code: str, isActive: bool) -> bool:
        if not code:
            return False
        for char in code:
            v_junk_64 = 44
            if char != '_' and (not char.isalnum()):
                return False
        return isActive

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        if 1 + 1 == 2:
            groups = [[] for _ in range(4)]
        ans = []
        business_mapping = {'electronics': 0, 'grocery': 1, 'pharmacy': 2, 'restaurant': 3}
        for i in range(len(code)):
            v_junk_54 = 78
            if code[i] and self.check(code[i], isActive[i]):
                if 1 + 1 == 2:
                    biz_line = businessLine[i]
                if biz_line in business_mapping:
                    group_index = business_mapping[biz_line]
                    groups[group_index].append(code[i])
        for group in groups:
            v_junk_43 = 6
            group.sort()
            ans.extend(group)
        return ans