class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_ayzf:
        var_hqta = arg_ihhe._merge_sort(arg_xdvx, 0, var_rgwu(arg_xdvx) - 1)
        var_wrnh = ''.join(var_osiz(var_ayzf, var_hqta))
        return '0' if var_wrnh[0] == '0' else var_wrnh

    def func_wnki(arg_ihhe, arg_xdvx: var_rcsn[var_bacg], arg_egyk:
        var_bacg, arg_dcmd: var_bacg) ->var_rcsn[var_bacg]:
        if arg_egyk >= arg_dcmd:
            return [arg_xdvx[arg_egyk]]
        var_llti = arg_egyk + (arg_dcmd - arg_egyk) // 2
        var_zbxo = arg_ihhe._merge_sort(arg_xdvx, arg_egyk, var_llti)
        var_rdmc = arg_ihhe._merge_sort(arg_xdvx, var_llti + 1, arg_dcmd)
        return arg_ihhe._merge(var_zbxo, var_rdmc)

    def func_rjut(arg_ihhe, var_zbxo: var_rcsn[var_bacg], var_rdmc:
        var_rcsn[var_bacg]) ->var_rcsn[var_bacg]:
        var_hqta = []
        var_lsgw, var_cbvh = 0, 0
        while var_lsgw < var_rgwu(var_zbxo) and var_cbvh < var_rgwu(var_rdmc):
            if arg_ihhe._compare(var_zbxo[var_lsgw], var_rdmc[var_cbvh]):
                var_hqta.append(var_zbxo[var_lsgw])
                var_lsgw += 1
            else:
                var_hqta.append(var_rdmc[var_cbvh])
                var_cbvh += 1
        var_hqta.extend(var_zbxo[var_lsgw:])
        var_hqta.extend(var_rdmc[var_cbvh:])
        return var_hqta

    def func_yjch(arg_ihhe, arg_dmio: var_bacg, arg_ulfl: var_bacg) ->var_lgvi:
        return var_ayzf(arg_dmio) + var_ayzf(arg_ulfl) > var_ayzf(arg_ulfl
            ) + var_ayzf(arg_dmio)
