class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg, arg_rcsn: var_bacg) ->var_ayzf:
        if var_hqta(arg_xdvx) != var_hqta(arg_rcsn):
            return False
        var_rgwu = var_hqta(arg_xdvx)
        for var_wrnh in var_osiz(var_rgwu):
            arg_xdvx = arg_xdvx[1:] + arg_xdvx[0]
            if arg_xdvx == arg_rcsn:
                return True
        return False
