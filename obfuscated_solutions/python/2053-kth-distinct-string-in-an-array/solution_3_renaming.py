class Solution:

    def func_udax(arg_ihhe, arg_xdvx: var_bacg[var_hqta], arg_rcsn: var_rgwu
        ) ->var_hqta:
        var_wrnh = {}
        for var_osiz in arg_xdvx:
            var_wrnh[var_osiz] = var_wrnh.get(var_osiz, 0) + 1
        for var_osiz in arg_xdvx:
            if var_wrnh[var_osiz] == 1:
                arg_rcsn -= 1
            if arg_rcsn == 0:
                return var_osiz
        return ''
