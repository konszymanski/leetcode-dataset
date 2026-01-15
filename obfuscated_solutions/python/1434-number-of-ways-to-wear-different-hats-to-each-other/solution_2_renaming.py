class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(var_wrnh)
        for var_osiz in var_ayzf(var_wnki(arg_xdvx)):
            for var_egyk in arg_xdvx[var_osiz]:
                var_hqta[var_egyk].append(var_osiz)
        var_dcmd = var_wnki(arg_xdvx)
        var_llti = 10 ** 9 + 7
        var_zbxo = 2 ** var_dcmd - 1
        var_rdmc = [([0] * (var_zbxo + 1)) for var_rjut in var_ayzf(42)]
        for var_osiz in var_ayzf(var_wnki(var_rdmc)):
            var_rdmc[var_osiz][var_zbxo] = 1
        for var_lsgw in var_ayzf(var_zbxo, -1, -1):
            for var_egyk in var_ayzf(40, 0, -1):
                var_cbvh = var_rdmc[var_egyk + 1][var_lsgw]
                for var_yjch in var_hqta[var_egyk]:
                    if var_lsgw & 1 << var_yjch == 0:
                        var_cbvh = (var_cbvh + var_rdmc[var_egyk + 1][
                            var_lsgw | 1 << var_yjch]) % var_llti
                var_rdmc[var_egyk][var_lsgw] = var_cbvh
        return var_rdmc[1][0]
