class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_hqta
        ) ->var_hqta:
        var_rgwu = 1
        var_wrnh = var_osiz(lambda : var_osiz(var_hqta))
        for var_ayzf in arg_xdvx:
            var_wrnh[var_ayzf % arg_rcsn][var_ayzf] += 1
        for var_wnki in var_wrnh.values():
            var_egyk = var_dcmd(var_wnki.items())
            var_rgwu *= arg_ihhe._count_beautiful_subsets(var_egyk,
                var_llti(var_egyk), arg_rcsn, 0)
        return var_rgwu - 1

    def func_zbxo(arg_ihhe, var_egyk, arg_rdmc, arg_rjut, arg_lsgw):
        if arg_lsgw == arg_rdmc:
            return 1
        var_cbvh = arg_ihhe._count_beautiful_subsets(var_egyk, arg_rdmc,
            arg_rjut, arg_lsgw + 1)
        var_yjch = (1 << var_egyk[arg_lsgw][1]) - 1
        if arg_lsgw + 1 < arg_rdmc and var_egyk[arg_lsgw + 1][0] - var_egyk[
            arg_lsgw][0] == arg_rjut:
            var_yjch *= arg_ihhe._count_beautiful_subsets(var_egyk,
                arg_rdmc, arg_rjut, arg_lsgw + 2)
        else:
            var_yjch *= arg_ihhe._count_beautiful_subsets(var_egyk,
                arg_rdmc, arg_rjut, arg_lsgw + 1)
        return var_cbvh + var_yjch
