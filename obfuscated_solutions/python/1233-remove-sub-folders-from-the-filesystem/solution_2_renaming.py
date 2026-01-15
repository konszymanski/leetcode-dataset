class Solution:

    def func_udax(arg_ihhe, arg_xdvx):
        arg_xdvx.sort()
        var_rcsn = [arg_xdvx[0]]
        for var_bacg in var_hqta(1, var_rgwu(arg_xdvx)):
            var_wrnh = var_rcsn[-1]
            var_wrnh += '/'
            if not arg_xdvx[var_bacg].startswith(var_wrnh):
                var_rcsn.append(arg_xdvx[var_bacg])
        return var_rcsn
