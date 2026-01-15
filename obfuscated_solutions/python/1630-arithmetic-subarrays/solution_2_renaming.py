class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta[var_rgwu], arg_rcsn:
        var_hqta[var_rgwu], arg_bacg: var_hqta[var_rgwu]) ->var_hqta[var_ulfl]:

        def func_wrnh(arg_osiz):
            var_ayzf = var_wnki(arg_osiz)
            var_egyk = var_dcmd(arg_osiz)
            if (var_egyk - var_ayzf) % (var_llti(arg_osiz) - 1) != 0:
                return False
            var_zbxo = (var_egyk - var_ayzf) / (var_llti(arg_osiz) - 1)
            var_rdmc = var_rjut(arg_osiz)
            var_lsgw = var_ayzf + var_zbxo
            while var_lsgw < var_egyk:
                if var_lsgw not in var_rdmc:
                    return False
                var_lsgw += var_zbxo
            return True
        var_cbvh = []
        for var_yjch in var_dmio(var_llti(arg_rcsn)):
            arg_osiz = arg_xdvx[arg_rcsn[var_yjch]:arg_bacg[var_yjch] + 1]
            var_cbvh.append(func_wrnh(arg_osiz))
        return var_cbvh
