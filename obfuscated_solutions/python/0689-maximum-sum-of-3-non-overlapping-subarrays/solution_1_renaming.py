class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_bacg[var_hqta]:
        var_rgwu = var_wrnh(arg_xdvx) - arg_rcsn + 1
        var_osiz = [var_ayzf(arg_xdvx[:arg_rcsn])]
        for var_wnki in var_egyk(arg_rcsn, var_wrnh(arg_xdvx)):
            var_osiz.append(var_osiz[-1] - arg_xdvx[var_wnki - arg_rcsn] +
                arg_xdvx[var_wnki])
        var_dcmd = [([-1] * 4) for var_llti in var_egyk(var_rgwu)]
        var_zbxo = []
        arg_ihhe._dp(var_osiz, arg_rcsn, 0, 3, var_dcmd)
        arg_ihhe._dfs(var_osiz, arg_rcsn, 0, 3, var_dcmd, var_zbxo)
        return var_zbxo

    def func_rdmc(arg_ihhe, var_osiz, arg_rcsn, arg_rjut, arg_lsgw, var_dcmd):
        if arg_lsgw == 0:
            return 0
        if arg_rjut >= var_wrnh(var_osiz):
            return var_cbvh('-inf') if arg_lsgw > 0 else 0
        if var_dcmd[arg_rjut][arg_lsgw] != -1:
            return var_dcmd[arg_rjut][arg_lsgw]
        var_yjch = var_osiz[arg_rjut] + arg_ihhe._dp(var_osiz, arg_rcsn, 
            arg_rjut + arg_rcsn, arg_lsgw - 1, var_dcmd)
        var_dmio = arg_ihhe._dp(var_osiz, arg_rcsn, arg_rjut + 1, arg_lsgw,
            var_dcmd)
        var_dcmd[arg_rjut][arg_lsgw] = var_ulfl(var_yjch, var_dmio)
        return var_dcmd[arg_rjut][arg_lsgw]

    def func_lgvi(arg_ihhe, var_osiz, arg_rcsn, arg_rjut, arg_lsgw,
        var_dcmd, var_zbxo):
        if arg_lsgw == 0 or arg_rjut >= var_wrnh(var_osiz):
            return
        var_yjch = var_osiz[arg_rjut] + arg_ihhe._dp(var_osiz, arg_rcsn, 
            arg_rjut + arg_rcsn, arg_lsgw - 1, var_dcmd)
        var_dmio = arg_ihhe._dp(var_osiz, arg_rcsn, arg_rjut + 1, arg_lsgw,
            var_dcmd)
        if var_yjch >= var_dmio:
            var_zbxo.append(arg_rjut)
            arg_ihhe._dfs(var_osiz, arg_rcsn, arg_rjut + arg_rcsn, arg_lsgw -
                1, var_dcmd, var_zbxo)
        else:
            arg_ihhe._dfs(var_osiz, arg_rcsn, arg_rjut + 1, arg_lsgw,
                var_dcmd, var_zbxo)
