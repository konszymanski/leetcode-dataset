class Solution(var_udax):

    def func_ihhe(arg_xdvx, arg_rcsn):
        var_bacg = var_hqta(arg_rcsn)
        var_rgwu, var_wrnh = [var_bacg] * var_bacg, [var_bacg] * var_bacg
        for var_osiz in var_ayzf(var_bacg):
            if arg_rcsn[var_osiz] == 1:
                var_rgwu[var_osiz] = 0
            elif var_osiz > 0:
                var_rgwu[var_osiz] = var_rgwu[var_osiz - 1] + 1
        for var_osiz in var_ayzf(var_bacg - 1, -1, -1):
            if arg_rcsn[var_osiz] == 1:
                var_wrnh[var_osiz] = 0
            elif var_osiz < var_bacg - 1:
                var_wrnh[var_osiz] = var_wrnh[var_osiz + 1] + 1
        return var_wnki(var_egyk(var_rgwu[var_osiz], var_wrnh[var_osiz]) for
            var_osiz, var_dcmd in var_llti(arg_rcsn) if not var_dcmd)
