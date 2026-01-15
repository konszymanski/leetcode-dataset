class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:
        var_rgwu = 10 ** 9 + 7
        var_wrnh = [0] * 26
        for var_osiz in arg_xdvx:
            var_wrnh[var_ayzf(var_osiz) - var_ayzf('a')] += 1
        for var_wnki in var_egyk(arg_rcsn):
            var_dcmd = [0] * 26
            var_dcmd[0] = var_wrnh[25]
            var_dcmd[1] = (var_wrnh[25] + var_wrnh[0]) % var_rgwu
            for var_llti in var_egyk(2, 26):
                var_dcmd[var_llti] = var_wrnh[var_llti - 1]
            var_wrnh = var_dcmd
        var_zbxo = var_rdmc(var_wrnh) % var_rgwu
        return var_zbxo
