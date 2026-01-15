class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        var_hqta = var_rgwu(arg_xdvx)
        var_wrnh = var_rgwu(arg_xdvx[0])
        var_osiz = [([False] * var_wrnh) for var_ayzf in var_wnki(var_hqta)]
        var_egyk = 0
        for var_dcmd in var_wnki(var_hqta):
            for var_llti in var_wnki(var_wrnh):
                if arg_xdvx[var_dcmd][var_llti] == 0 and not var_osiz[var_dcmd
                    ][var_llti] and arg_ihhe.dfs(var_dcmd, var_llti,
                    var_hqta, var_wrnh, arg_xdvx, var_osiz):
                    var_egyk += 1
        return var_egyk

    def func_zbxo(arg_ihhe, arg_rdmc: var_bacg, arg_rjut: var_bacg,
        var_hqta: var_bacg, var_wrnh: var_bacg, arg_xdvx: var_rcsn[var_rcsn
        [var_bacg]], var_osiz: var_rcsn[var_rcsn[var_lsgw]]) ->var_lsgw:
        if (arg_rdmc < 0 or arg_rdmc >= var_hqta or arg_rjut < 0 or 
            arg_rjut >= var_wrnh):
            return False
        if arg_xdvx[arg_rdmc][arg_rjut] == 1 or var_osiz[arg_rdmc][arg_rjut]:
            return True
        var_osiz[arg_rdmc][arg_rjut] = True
        var_cbvh = True
        var_yjch = [0, 1, 0, -1]
        var_dmio = [-1, 0, 1, 0]
        for var_dcmd in var_wnki(4):
            var_ulfl = arg_rdmc + var_yjch[var_dcmd]
            var_lgvi = arg_rjut + var_dmio[var_dcmd]
            if not arg_ihhe.dfs(var_ulfl, var_lgvi, var_hqta, var_wrnh,
                arg_xdvx, var_osiz):
                var_cbvh = False
        return var_cbvh
