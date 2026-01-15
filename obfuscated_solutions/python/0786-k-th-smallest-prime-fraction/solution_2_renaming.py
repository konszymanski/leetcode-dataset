class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = []

        def func_hqta(arg_rgwu, arg_wrnh):
            return arg_rgwu[0] - arg_wrnh[0]
        for var_osiz in var_ayzf(var_wnki(arg_xdvx) - 1):
            var_egyk.heappush(var_bacg, (arg_xdvx[var_osiz] / arg_xdvx[-1],
                var_osiz, var_wnki(arg_xdvx) - 1))
        for var_dcmd in var_ayzf(arg_rcsn - 1):
            var_llti = var_egyk.heappop(var_bacg)
            var_zbxo = var_llti[1]
            var_rdmc = var_llti[2] - 1
            if var_rdmc > var_zbxo:
                var_egyk.heappush(var_bacg, (arg_xdvx[var_zbxo] / arg_xdvx[
                    var_rdmc], var_zbxo, var_rdmc))
        var_rjut = var_egyk.heappop(var_bacg)
        return [arg_xdvx[var_rjut[1]], arg_xdvx[var_rjut[2]]]
