class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_dcmd:
        var_hqta = 0
        var_rgwu, var_wrnh = var_osiz(arg_xdvx), var_osiz(arg_rcsn)
        for var_ayzf in var_wnki(var_rgwu):
            if var_hqta < var_wrnh and (arg_xdvx[var_ayzf] == arg_rcsn[
                var_hqta] or var_egyk(arg_xdvx[var_ayzf]) + 1 == var_egyk(
                arg_rcsn[var_hqta]) or var_egyk(arg_xdvx[var_ayzf]) - 25 ==
                var_egyk(arg_rcsn[var_hqta])):
                var_hqta += 1
        return var_hqta == var_wrnh
