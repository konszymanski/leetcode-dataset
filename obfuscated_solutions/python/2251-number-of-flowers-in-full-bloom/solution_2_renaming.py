from sortedcontainers import SortedDict


class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_bacg[var_hqta]],
        arg_rcsn: var_bacg[var_hqta]) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh({(0): 0})
        for var_osiz, var_ayzf in arg_xdvx:
            var_rgwu[var_osiz] = var_rgwu.get(var_osiz, 0) + 1
            var_rgwu[var_ayzf + 1] = var_rgwu.get(var_ayzf + 1, 0) - 1
        var_wnki = []
        var_egyk = []
        var_dcmd = 0
        for var_llti, var_zbxo in var_rgwu.items():
            var_wnki.append(var_llti)
            var_dcmd += var_zbxo
            var_egyk.append(var_dcmd)
        var_rdmc = []
        for var_rjut in arg_rcsn:
            var_lsgw = var_cbvh(var_wnki, var_rjut) - 1
            var_rdmc.append(var_egyk[var_lsgw])
        return var_rdmc
