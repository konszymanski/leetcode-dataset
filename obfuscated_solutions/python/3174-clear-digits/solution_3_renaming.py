class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_rcsn) ->var_rcsn:
        var_bacg = 0
        arg_xdvx = var_hqta(arg_xdvx)
        for var_rgwu in var_wrnh(var_osiz(arg_xdvx)):
            if arg_xdvx[var_rgwu].isdigit():
                var_bacg -= 1
            else:
                arg_xdvx[var_bacg] = arg_xdvx[var_rgwu]
                var_bacg += 1
        arg_xdvx = arg_xdvx[:var_bacg]
        return ''.join(arg_xdvx)
