class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = var_wrnh(arg_xdvx)
        var_osiz = [(0, -1)]
        var_ayzf = 0
        var_wnki = var_egyk('inf')
        for var_dcmd in var_llti(var_rgwu):
            var_ayzf += arg_xdvx[var_dcmd]
            while var_osiz and var_ayzf <= var_osiz[-1][0]:
                var_osiz.pop()
            var_osiz.append((var_ayzf, var_dcmd))
            var_zbxo = arg_ihhe._find_candidate_index(var_osiz, var_ayzf -
                arg_rcsn)
            if var_zbxo != -1:
                var_wnki = var_rdmc(var_wnki, var_dcmd - var_osiz[var_zbxo][1])
        return var_wnki if var_wnki != var_egyk('inf') else -1

    def func_rjut(arg_ihhe, arg_xdvx: var_bacg[var_cbvh[var_hqta, var_hqta]
        ], arg_lsgw: var_hqta) ->var_hqta:
        var_yjch, var_dmio = 0, var_wrnh(arg_xdvx) - 1
        while var_yjch <= var_dmio:
            var_ulfl = var_yjch + (var_dmio - var_yjch) // 2
            if arg_xdvx[var_ulfl][0] <= arg_lsgw:
                var_yjch = var_ulfl + 1
            else:
                var_dmio = var_ulfl - 1
        return var_dmio
