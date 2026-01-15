class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = 0
        while arg_xdvx > 0:
            var_rcsn += arg_xdvx % 10
            arg_xdvx //= 10
        return var_rcsn

    def func_bacg(arg_ihhe, arg_hqta):
        var_rgwu = [[] for var_wrnh in var_osiz(82)]
        var_ayzf = -1
        for var_wnki in arg_hqta:
            var_rcsn = arg_ihhe.calculate_digit_sum(var_wnki)
            var_egyk.heappush(var_rgwu[var_rcsn], var_wnki)
            if var_dcmd(var_rgwu[var_rcsn]) > 2:
                var_egyk.heappop(var_rgwu[var_rcsn])
        for var_llti in var_rgwu:
            if var_dcmd(var_llti) == 2:
                var_zbxo = var_egyk.heappop(var_llti)
                var_rdmc = var_egyk.heappop(var_llti)
                var_ayzf = var_rjut(var_ayzf, var_zbxo + var_rdmc)
        return var_ayzf
