class Solution:
    var_udax = -1

    def func_ihhe(arg_xdvx, arg_rcsn, arg_bacg, arg_hqta, arg_rgwu):
        arg_bacg[arg_rcsn] = True
        for var_wrnh in arg_hqta[arg_rcsn]:
            if not arg_bacg[var_wrnh]:
                arg_rgwu[var_wrnh] = arg_rcsn
                arg_xdvx._DFS(var_wrnh, arg_bacg, arg_hqta, arg_rgwu)
            elif var_wrnh != arg_rgwu[arg_rcsn] and arg_xdvx.cycle_start == -1:
                arg_xdvx.cycle_start = var_wrnh
                arg_rgwu[var_wrnh] = arg_rcsn

    def func_osiz(arg_xdvx, arg_ayzf):
        var_wnki = var_egyk(arg_ayzf)
        arg_bacg = [False] * var_wnki
        arg_rgwu = [-1] * var_wnki
        arg_hqta = [[] for var_dcmd in var_llti(var_wnki)]
        for var_zbxo in arg_ayzf:
            arg_hqta[var_zbxo[0] - 1].append(var_zbxo[1] - 1)
            arg_hqta[var_zbxo[1] - 1].append(var_zbxo[0] - 1)
        arg_xdvx._DFS(0, arg_bacg, arg_hqta, arg_rgwu)
        var_rdmc = {}
        var_rjut = arg_xdvx.cycle_start
        while True:
            var_rdmc[var_rjut] = 1
            var_rjut = arg_rgwu[var_rjut]
            if var_rjut == arg_xdvx.cycle_start:
                break
        for var_lsgw in var_llti(var_egyk(arg_ayzf) - 1, -1, -1):
            if arg_ayzf[var_lsgw][0] - 1 in var_rdmc and arg_ayzf[var_lsgw][1
                ] - 1 in var_rdmc:
                return arg_ayzf[var_lsgw]
        return []
