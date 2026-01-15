class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu = [[] for var_wrnh in var_osiz(arg_xdvx)]
        var_ayzf = var_wnki(var_bacg)
        for var_egyk in var_osiz(arg_xdvx):
            var_rgwu[var_egyk] = [var_egyk]
        for var_dcmd, var_llti in arg_rcsn:
            var_rgwu[var_dcmd].append(var_llti)
            var_rgwu[var_llti].append(var_dcmd)
        for var_egyk in var_osiz(arg_xdvx):
            var_zbxo = var_rdmc(var_rjut(var_rgwu[var_egyk]))
            var_ayzf[var_zbxo] += 1
        return var_lsgw(1 for var_zbxo, var_cbvh in var_ayzf.items() if 
            var_yjch(var_zbxo) == var_cbvh)
