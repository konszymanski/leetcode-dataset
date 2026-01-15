class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_hqta) ->var_hqta:

        def func_rgwu(arg_wrnh: var_hqta, arg_osiz: var_hqta) ->var_hqta:
            return (arg_wrnh & 1) << 1 | arg_osiz & 1
        var_ayzf = var_wnki(arg_xdvx)
        var_egyk = var_dcmd('-inf')
        for var_llti in ['0', '1', '2', '3', '4']:
            for var_zbxo in ['0', '1', '2', '3', '4']:
                if var_llti == var_zbxo:
                    continue
                var_rdmc = [var_dcmd('inf')] * 4
                arg_wrnh = arg_osiz = 0
                var_rjut = var_lsgw = 0
                var_cbvh = -1
                for var_yjch in var_dmio(var_ayzf):
                    arg_wrnh += arg_xdvx[var_yjch] == var_llti
                    arg_osiz += arg_xdvx[var_yjch] == var_zbxo
                    while (var_yjch - var_cbvh >= arg_rcsn and arg_osiz -
                        var_lsgw >= 2):
                        var_ulfl = func_rgwu(var_rjut, var_lsgw)
                        var_rdmc[var_ulfl] = var_lgvi(var_rdmc[var_ulfl], 
                            var_rjut - var_lsgw)
                        var_cbvh += 1
                        var_rjut += arg_xdvx[var_cbvh] == var_llti
                        var_lsgw += arg_xdvx[var_cbvh] == var_zbxo
                    var_wvuc = func_rgwu(arg_wrnh, arg_osiz)
                    if var_rdmc[var_wvuc ^ 2] != var_dcmd('inf'):
                        var_egyk = var_tufr(var_egyk, arg_wrnh - arg_osiz -
                            var_rdmc[var_wvuc ^ 2])
        return var_egyk
