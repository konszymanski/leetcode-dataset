class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_hqta, arg_rcsn: var_rgwu[var_rgwu
        [var_hqta]], arg_bacg: var_hqta) ->var_rgwu[var_hqta]:
        var_wrnh = var_osiz(var_ayzf)
        for var_wnki, var_egyk, var_dcmd in arg_rcsn:
            var_wrnh[var_wnki].append((var_dcmd, var_egyk))
            var_wrnh[var_egyk].append((var_dcmd, var_wnki))
        var_llti = []
        var_zbxo(var_llti, (0, 0))
        var_zbxo(var_llti, (0, arg_bacg))
        var_rdmc = [False] * arg_xdvx
        while var_llti:
            var_rjut, var_lsgw = var_cbvh(var_llti)
            if var_rdmc[var_lsgw]:
                continue
            var_rdmc[var_lsgw] = True
            for var_dcmd, var_yjch in var_wrnh[var_lsgw]:
                if not var_rdmc[var_yjch] and var_dcmd >= var_rjut:
                    var_zbxo(var_llti, (var_dcmd, var_yjch))
        return [var_dmio for var_dmio in var_ulfl(arg_xdvx) if var_rdmc[
            var_dmio]]
