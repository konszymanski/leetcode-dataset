class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_ayzf:
        var_bacg = var_hqta(arg_xdvx)
        var_rgwu = 0
        for var_wrnh in var_bacg.values():
            if var_wrnh % 2 == 1:
                var_rgwu += var_wrnh - 1
            else:
                var_rgwu += var_wrnh - 2
        return var_osiz(arg_xdvx) - var_rgwu
