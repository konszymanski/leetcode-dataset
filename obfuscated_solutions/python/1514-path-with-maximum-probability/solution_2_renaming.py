class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_wrnh, arg_rcsn: var_osiz[var_osiz
        [var_wrnh]], arg_bacg: var_osiz[var_ayzf], arg_hqta: var_wrnh,
        arg_rgwu: var_wrnh) ->var_ayzf:
        var_wnki = var_egyk(var_dcmd)
        for var_llti, (var_zbxo, var_rdmc) in var_rjut(arg_rcsn):
            var_wnki[var_zbxo].append([var_rdmc, arg_bacg[var_llti]])
            var_wnki[var_rdmc].append([var_zbxo, arg_bacg[var_llti]])
        var_lsgw = [0.0] * arg_xdvx
        var_lsgw[arg_hqta] = 1.0
        var_cbvh = var_yjch([arg_hqta])
        while var_cbvh:
            var_dmio = var_cbvh.popleft()
            for var_ulfl, var_lgvi in var_wnki[var_dmio]:
                if var_lsgw[var_dmio] * var_lgvi > var_lsgw[var_ulfl]:
                    var_lsgw[var_ulfl] = var_lsgw[var_dmio] * var_lgvi
                    var_cbvh.append(var_ulfl)
        return var_lsgw[arg_rgwu]
