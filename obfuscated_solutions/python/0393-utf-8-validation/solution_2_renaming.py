class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        """
        :type data: List[int]
        :rtype: bool
        """
        var_rcsn = 0
        var_bacg = 1 << 7
        var_hqta = 1 << 6
        for var_rgwu in arg_xdvx:
            var_wrnh = 1 << 7
            if var_rcsn == 0:
                while var_wrnh & var_rgwu:
                    var_rcsn += 1
                    var_wrnh = var_wrnh >> 1
                if var_rcsn == 0:
                    continue
                if var_rcsn == 1 or var_rcsn > 4:
                    return False
            elif not (var_rgwu & var_bacg and not var_rgwu & var_hqta):
                return False
            var_rcsn -= 1
        return var_rcsn == 0
