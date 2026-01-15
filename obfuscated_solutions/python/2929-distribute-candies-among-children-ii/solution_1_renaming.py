class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_bacg:
        var_hqta = 0
        for var_rgwu in var_wrnh(var_osiz(arg_rcsn, arg_xdvx) + 1):
            if arg_xdvx - var_rgwu > 2 * arg_rcsn:
                continue
            var_hqta += var_osiz(arg_xdvx - var_rgwu, arg_rcsn) - var_ayzf(
                0, arg_xdvx - var_rgwu - arg_rcsn) + 1
        return var_hqta
