class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = ['999', '888', '777', '666', '555', '444', '333', '222',
            '111', '000']

        def func_hqta(arg_rgwu):
            for var_wrnh in var_osiz(var_ayzf(arg_xdvx) - 2):
                if arg_xdvx[var_wrnh] == arg_rgwu[0] and arg_xdvx[var_wrnh + 1
                    ] == arg_rgwu[1] and arg_xdvx[var_wrnh + 2] == arg_rgwu[2]:
                    return True
            return False
        for arg_rgwu in var_bacg:
            if func_hqta(arg_rgwu):
                return arg_rgwu
        return ''
