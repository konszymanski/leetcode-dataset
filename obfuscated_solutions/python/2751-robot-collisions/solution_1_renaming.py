class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_wrnh) ->var_hqta[var_rgwu]:
        var_osiz = var_ayzf(arg_xdvx)
        var_wnki = var_egyk(var_dcmd(var_osiz))
        var_llti = []
        var_zbxo = var_rdmc()
        var_wnki.sort(key=lambda x: arg_xdvx[var_rjut])
        for var_lsgw in var_wnki:
            if arg_bacg[var_lsgw] == 'R':
                var_zbxo.append(var_lsgw)
            else:
                while var_zbxo and arg_rcsn[var_lsgw] > 0:
                    var_cbvh = var_zbxo.pop()
                    if arg_rcsn[var_cbvh] > arg_rcsn[var_lsgw]:
                        arg_rcsn[var_cbvh] -= 1
                        arg_rcsn[var_lsgw] = 0
                        var_zbxo.append(var_cbvh)
                    elif arg_rcsn[var_cbvh] < arg_rcsn[var_lsgw]:
                        arg_rcsn[var_lsgw] -= 1
                        arg_rcsn[var_cbvh] = 0
                    else:
                        arg_rcsn[var_lsgw] = 0
                        arg_rcsn[var_cbvh] = 0
        for var_yjch in var_dcmd(var_osiz):
            if arg_rcsn[var_yjch] > 0:
                var_llti.append(arg_rcsn[var_yjch])
        return var_llti
