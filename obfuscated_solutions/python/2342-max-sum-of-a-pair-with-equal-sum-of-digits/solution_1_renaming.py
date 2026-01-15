class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        while arg_xdvx > 0:
            var_rcsn += arg_xdvx % 10
            arg_xdvx //= 10
        return var_rcsn

    def func_bacg(arg_ihhe, arg_hqta):
        var_rgwu = []
        for var_wrnh in arg_hqta:
            var_rcsn = arg_ihhe.calculate_digit_sum(var_wrnh)
            var_rgwu.append((var_rcsn, var_wrnh))
        var_rgwu.sort()
        var_osiz = -1
        for var_ayzf in var_wnki(1, var_egyk(var_rgwu)):
            var_dcmd = var_rgwu[var_ayzf][0]
            var_llti = var_rgwu[var_ayzf - 1][0]
            if var_dcmd == var_llti:
                var_zbxo = var_rgwu[var_ayzf][1] + var_rgwu[var_ayzf - 1][1]
                var_osiz = var_rdmc(var_osiz, var_zbxo)
        return var_osiz
