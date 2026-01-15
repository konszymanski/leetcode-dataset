class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_hqta) ->var_rgwu[var_hqta]:
        var_wrnh = var_osiz(var_ayzf)
        for var_wnki, var_egyk, var_dcmd in arg_rcsn:
            var_wrnh[var_wnki].append((var_dcmd, var_egyk))
            var_wrnh[var_egyk].append((var_dcmd, var_wnki))
        var_llti = [var_zbxo] * arg_xdvx
        var_llti[0] = 0
        var_llti[arg_bacg] = 0
        var_rdmc = [(0, 0), (arg_bacg, 0)]
        while var_rdmc:
            var_rjut, var_lsgw = var_rdmc.pop()
            for var_dcmd, var_cbvh in var_wrnh[var_rjut]:
                if var_dcmd >= var_lsgw and var_llti[var_cbvh] > var_dcmd:
                    var_llti[var_cbvh] = var_dcmd
                    var_rdmc.append((var_cbvh, var_dcmd))
        return [var_yjch for var_yjch in var_dmio(arg_xdvx) if var_llti[
            var_yjch] != var_zbxo]
