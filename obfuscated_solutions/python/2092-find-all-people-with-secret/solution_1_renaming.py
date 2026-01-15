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
        var_rdmc = var_rjut()
        var_rdmc.append((0, 0))
        var_rdmc.append((arg_bacg, 0))
        while var_rdmc:
            var_lsgw, var_cbvh = var_rdmc.popleft()
            for var_dcmd, var_yjch in var_wrnh[var_lsgw]:
                if var_dcmd >= var_cbvh and var_llti[var_yjch] > var_dcmd:
                    var_llti[var_yjch] = var_dcmd
                    var_rdmc.append((var_yjch, var_dcmd))
        return [var_dmio for var_dmio in var_ulfl(arg_xdvx) if var_llti[
            var_dmio] != var_zbxo]
