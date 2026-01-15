class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        """
        :type word: str
        :rtype: int
        """
        var_bacg = {}
        var_bacg[0] = 1
        var_hqta = 0
        var_rgwu = 0
        for var_wrnh in arg_rcsn:
            var_osiz = var_ayzf(var_wrnh) - 97
            var_hqta ^= 1 << var_osiz
            if var_hqta in var_bacg:
                var_rgwu += var_bacg[var_hqta]
                var_bacg[var_hqta] += 1
            else:
                var_bacg[var_hqta] = 1
            for var_wnki in var_egyk(0, 10):
                if var_hqta ^ 1 << var_wnki in var_bacg:
                    var_rgwu += var_bacg[var_hqta ^ 1 << var_wnki]
        return var_rgwu
