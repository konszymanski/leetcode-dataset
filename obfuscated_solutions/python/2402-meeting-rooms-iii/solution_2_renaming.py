class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta[var_hqta
        [var_bacg]]) ->var_bacg:
        var_rgwu, var_wrnh = var_osiz(var_ayzf(arg_xdvx)), []
        var_wnki(var_rgwu)
        var_egyk = [0] * arg_xdvx
        for var_dcmd, var_llti in var_zbxo(arg_rcsn):
            while var_wrnh and var_wrnh[0][0] <= var_dcmd:
                var_rdmc, var_rjut = var_lsgw(var_wrnh)
                var_cbvh(var_rgwu, var_rjut)
            if var_rgwu:
                var_rjut = var_lsgw(var_rgwu)
                var_cbvh(var_wrnh, [var_llti, var_rjut])
            else:
                var_yjch, var_rjut = var_lsgw(var_wrnh)
                var_cbvh(var_wrnh, [var_yjch + var_llti - var_dcmd, var_rjut])
            var_egyk[var_rjut] += 1
        return var_egyk.index(var_dmio(var_egyk))
