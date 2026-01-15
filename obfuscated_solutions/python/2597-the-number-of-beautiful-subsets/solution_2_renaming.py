class Solution:

    def func_udax(arg_ihhe, arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(var_rgwu)
        arg_xdvx.sort()
        return arg_ihhe._count_beautiful_subsets(arg_xdvx, arg_rcsn,
            var_bacg, 0) - 1

    def func_wrnh(arg_ihhe, arg_xdvx, arg_osiz, var_bacg, arg_ayzf):
        if arg_ayzf == var_wnki(arg_xdvx):
            return 1
        var_egyk = arg_ihhe._count_beautiful_subsets(arg_xdvx, arg_osiz,
            var_bacg, arg_ayzf + 1)
        if arg_xdvx[arg_ayzf] - arg_osiz not in var_bacg:
            var_bacg[arg_xdvx[arg_ayzf]] += 1
            var_egyk += arg_ihhe._count_beautiful_subsets(arg_xdvx,
                arg_osiz, var_bacg, arg_ayzf + 1)
            var_bacg[arg_xdvx[arg_ayzf]] -= 1
            if var_bacg[arg_xdvx[arg_ayzf]] == 0:
                del var_bacg[arg_xdvx[arg_ayzf]]
        return var_egyk
