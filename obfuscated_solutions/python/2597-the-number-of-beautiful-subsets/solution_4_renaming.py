class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn) ->var_hqta:
        var_rgwu = 1
        var_wrnh = var_osiz(lambda : var_osiz(var_hqta))
        for var_ayzf in arg_xdvx:
            var_wrnh[var_ayzf % arg_rcsn][var_ayzf] += 1
        for var_wnki in var_wrnh.values():
            var_egyk = var_dcmd(var_wnki.items())
            var_llti = [-1] * var_zbxo(var_egyk)
            var_rgwu *= arg_ihhe._count_beautiful_subsets(var_egyk,
                arg_rcsn, 0, var_llti)
        return var_rgwu - 1

    def func_rdmc(arg_ihhe, arg_rjut: var_bacg[var_bacg[var_hqta]],
        arg_lsgw: var_hqta, arg_cbvh: var_hqta, var_llti: var_bacg[var_hqta]
        ) ->var_hqta:
        if arg_cbvh == var_zbxo(arg_rjut):
            return 1
        if var_llti[arg_cbvh] != -1:
            return var_llti[arg_cbvh]
        var_yjch = arg_ihhe._count_beautiful_subsets(arg_rjut, arg_lsgw, 
            arg_cbvh + 1, var_llti)
        var_dmio = (1 << arg_rjut[arg_cbvh][1]) - 1
        if arg_cbvh + 1 < var_zbxo(arg_rjut) and arg_rjut[arg_cbvh + 1][0
            ] - arg_rjut[arg_cbvh][0] == arg_lsgw:
            var_dmio *= arg_ihhe._count_beautiful_subsets(arg_rjut,
                arg_lsgw, arg_cbvh + 2, var_llti)
        else:
            var_dmio *= arg_ihhe._count_beautiful_subsets(arg_rjut,
                arg_lsgw, arg_cbvh + 1, var_llti)
        var_llti[arg_cbvh] = var_yjch + var_dmio
        return var_llti[arg_cbvh]
