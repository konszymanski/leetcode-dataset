class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn[var_bacg]) ->var_bacg:
        var_hqta = 0
        for var_rgwu in arg_xdvx:
            var_hqta |= var_rgwu
        return arg_ihhe._count_subsets(arg_xdvx, 0, 0, var_hqta)

    def func_wrnh(arg_ihhe, arg_xdvx: var_rcsn[var_bacg], arg_osiz:
        var_bacg, arg_ayzf: var_bacg, arg_wnki: var_bacg) ->var_bacg:
        if arg_osiz == var_egyk(arg_xdvx):
            return 1 if arg_ayzf == arg_wnki else 0
        var_dcmd = arg_ihhe._count_subsets(arg_xdvx, arg_osiz + 1, arg_ayzf,
            arg_wnki)
        var_llti = arg_ihhe._count_subsets(arg_xdvx, arg_osiz + 1, arg_ayzf |
            arg_xdvx[arg_osiz], arg_wnki)
        return var_dcmd + var_llti
