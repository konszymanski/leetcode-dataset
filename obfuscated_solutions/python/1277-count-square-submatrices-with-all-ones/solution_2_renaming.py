class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn, arg_bacg, arg_hqta):
        if arg_xdvx >= var_rgwu(arg_bacg) or arg_rcsn >= var_rgwu(arg_bacg[0]):
            return 0
        if arg_bacg[arg_xdvx][arg_rcsn] == 0:
            return 0
        if arg_hqta[arg_xdvx][arg_rcsn] != -1:
            return arg_hqta[arg_xdvx][arg_rcsn]
        var_wrnh = arg_ihhe.solve(arg_xdvx, arg_rcsn + 1, arg_bacg, arg_hqta)
        var_osiz = arg_ihhe.solve(arg_xdvx + 1, arg_rcsn + 1, arg_bacg,
            arg_hqta)
        var_ayzf = arg_ihhe.solve(arg_xdvx + 1, arg_rcsn, arg_bacg, arg_hqta)
        arg_hqta[arg_xdvx][arg_rcsn] = 1 + var_wnki(var_wrnh, var_wnki(
            var_osiz, var_ayzf))
        return arg_hqta[arg_xdvx][arg_rcsn]

    def func_egyk(arg_ihhe, arg_dcmd: var_llti[var_llti[var_zbxo]]) ->var_zbxo:
        var_rdmc = 0
        arg_hqta = [[(-1) for var_rjut in var_lsgw(var_rgwu(arg_dcmd[0]))] for
            var_rjut in var_lsgw(var_rgwu(arg_dcmd))]
        for arg_xdvx in var_lsgw(var_rgwu(arg_dcmd)):
            for arg_rcsn in var_lsgw(var_rgwu(arg_dcmd[0])):
                var_rdmc += arg_ihhe.solve(arg_xdvx, arg_rcsn, arg_dcmd,
                    arg_hqta)
        return var_rdmc
