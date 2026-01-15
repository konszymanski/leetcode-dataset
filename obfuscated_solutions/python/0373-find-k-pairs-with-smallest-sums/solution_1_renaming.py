class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_rgwu) ->var_hqta[var_hqta[var_rgwu]]:
        from heapq import heappush, heappop
        var_wrnh = var_osiz(arg_xdvx)
        var_ayzf = var_osiz(arg_rcsn)
        var_wnki = []
        var_egyk = var_dcmd()
        var_llti = [(arg_xdvx[0] + arg_rcsn[0], (0, 0))]
        var_egyk.add((0, 0))
        while arg_bacg > 0 and var_llti:
            var_zbxo, (var_rdmc, var_rjut) = var_lsgw(var_llti)
            var_wnki.append([arg_xdvx[var_rdmc], arg_rcsn[var_rjut]])
            if var_rdmc + 1 < var_wrnh and (var_rdmc + 1, var_rjut
                ) not in var_egyk:
                var_cbvh(var_llti, (arg_xdvx[var_rdmc + 1] + arg_rcsn[
                    var_rjut], (var_rdmc + 1, var_rjut)))
                var_egyk.add((var_rdmc + 1, var_rjut))
            if var_rjut + 1 < var_ayzf and (var_rdmc, var_rjut + 1
                ) not in var_egyk:
                var_cbvh(var_llti, (arg_xdvx[var_rdmc] + arg_rcsn[var_rjut +
                    1], (var_rdmc, var_rjut + 1)))
                var_egyk.add((var_rdmc, var_rjut + 1))
            arg_bacg = arg_bacg - 1
        return var_wnki
