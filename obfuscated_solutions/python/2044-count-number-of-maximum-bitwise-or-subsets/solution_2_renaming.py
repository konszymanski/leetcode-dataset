class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        var_rgwu = var_wrnh(arg_xdvx)
        for var_osiz in arg_xdvx:
            var_hqta |= var_osiz
        var_ayzf = [([-1] * (var_hqta + 1)) for var_wnki in var_egyk(var_rgwu)]
        return arg_ihhe._count_subsets_recursive(arg_xdvx, 0, 0, var_hqta,
            var_ayzf)

    def func_dcmd(arg_ihhe, arg_xdvx: var_rcsn[var_bacg], arg_llti:
        var_bacg, arg_zbxo: var_bacg, arg_rdmc: var_bacg, var_ayzf:
        var_rcsn[var_rcsn[var_bacg]]) ->var_bacg:
        if arg_llti == var_wrnh(arg_xdvx):
            return 1 if arg_zbxo == arg_rdmc else 0
        if var_ayzf[arg_llti][arg_zbxo] != -1:
            return var_ayzf[arg_llti][arg_zbxo]
        var_rjut = arg_ihhe._count_subsets_recursive(arg_xdvx, arg_llti + 1,
            arg_zbxo, arg_rdmc, var_ayzf)
        var_lsgw = arg_ihhe._count_subsets_recursive(arg_xdvx, arg_llti + 1,
            arg_zbxo | arg_xdvx[arg_llti], arg_rdmc, var_ayzf)
        var_ayzf[arg_llti][arg_zbxo] = var_rjut + var_lsgw
        return var_ayzf[arg_llti][arg_zbxo]
