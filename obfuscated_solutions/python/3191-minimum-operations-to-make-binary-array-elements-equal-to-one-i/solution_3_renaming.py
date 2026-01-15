class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        var_rcsn = var_bacg(arg_xdvx)
        var_hqta = 0
        for var_rgwu in var_wrnh(var_rcsn - 2):
            if arg_xdvx[var_rgwu] == 0:
                arg_xdvx[var_rgwu] = 1
                arg_xdvx[var_rgwu + 1] = 1 if arg_xdvx[var_rgwu + 1
                    ] == 0 else 0
                arg_xdvx[var_rgwu + 2] = 1 if arg_xdvx[var_rgwu + 2
                    ] == 0 else 0
                var_hqta += 1
        if arg_xdvx[var_rcsn - 2] == 0 or arg_xdvx[var_rcsn - 1] == 0:
            return -1
        return var_hqta
