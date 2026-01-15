class Solution:
    var_udax = [-1, 0, 1]

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta, arg_rgwu):
        var_wrnh, var_osiz = var_ayzf(arg_hqta), var_ayzf(arg_hqta[0])
        if arg_rgwu[arg_rcsn][arg_bacg] != -1:
            return arg_rgwu[arg_rcsn][arg_bacg]
        var_wnki = 0
        for var_egyk in arg_xdvx.dirs:
            var_dcmd, var_llti = arg_rcsn + var_egyk, arg_bacg + 1
            if (0 <= var_dcmd < var_wrnh and 0 <= var_llti < var_osiz and 
                arg_hqta[arg_rcsn][arg_bacg] < arg_hqta[var_dcmd][var_llti]):
                var_wnki = var_zbxo(var_wnki, 1 + arg_xdvx.DFS(var_dcmd,
                    var_llti, arg_hqta, arg_rgwu))
        arg_rgwu[arg_rcsn][arg_bacg] = var_wnki
        return var_wnki

    def func_rdmc(arg_xdvx, arg_hqta):
        var_wrnh, var_osiz = var_ayzf(arg_hqta), var_ayzf(arg_hqta[0])
        arg_rgwu = [([-1] * var_osiz) for var_rjut in var_lsgw(var_wrnh)]
        var_wnki = 0
        for var_cbvh in var_lsgw(var_wrnh):
            var_yjch = arg_xdvx.DFS(var_cbvh, 0, arg_hqta, arg_rgwu)
            var_wnki = var_zbxo(var_wnki, var_yjch)
        return var_wnki
