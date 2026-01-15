class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rgwu, arg_rcsn: var_wrnh[var_wrnh
        [var_rgwu]], arg_bacg: var_wrnh[var_rgwu], arg_hqta: var_rgwu
        ) ->var_rgwu:
        var_osiz = [[] for var_ayzf in var_wnki(arg_xdvx)]
        for var_egyk, var_dcmd in arg_rcsn:
            var_osiz[var_egyk].append(var_dcmd)
            var_osiz[var_dcmd].append(var_egyk)
        var_llti = [0]
        arg_ihhe.dfs(0, -1, var_osiz, values, arg_hqta, var_llti)
        return var_llti[0]

    def func_zbxo(arg_ihhe, arg_rdmc: var_rgwu, arg_rjut: var_rgwu,
        var_osiz: var_wrnh[var_wrnh[var_rgwu]], arg_lsgw: var_wrnh[var_rgwu
        ], arg_hqta: var_rgwu, var_llti: var_wrnh[var_rgwu]) ->var_rgwu:
        var_cbvh = 0
        for var_yjch in var_osiz[arg_rdmc]:
            if var_yjch != arg_rjut:
                var_cbvh += arg_ihhe.dfs(var_yjch, arg_rdmc, var_osiz,
                    arg_lsgw, arg_hqta, var_llti)
                var_cbvh %= arg_hqta
        var_cbvh += arg_lsgw[arg_rdmc]
        var_cbvh %= arg_hqta
        if var_cbvh == 0:
            var_llti[0] += 1
        return var_cbvh
